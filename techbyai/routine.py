import json
from time import time
from datetime import datetime, timedelta
from random import randint
from textwrap import dedent
from concurrent.futures import ThreadPoolExecutor
from typing import Any
from .assistant import Assistant
from .color_logger import get_logger
from .utils import flatten


class Routine:
    NUM_OF_REPORTERS = 4
    TOPICS = dedent(
        """
        Foundation Models, AI Ethics and Bias, AI in Healthcare, Generative AI, AI in Creative Industries,
        AI Regulation and Policy, AI and Cybersecurity, AI in Education, AI and Climate Change, AI in Robotics,
        AI in Gaming, Promising startups in Generative AI, Distinguished companies (like OpenAI, Anthropic, Mistral, 
        Google, Cohere, Microsoft, Amazon, Midjourney, Stability, etc.)
        """.strip())

    def __init__(self) -> None:
        self.editor: Assistant
        self.reporters: list[Assistant] = []
        self.logger = get_logger()
        self.start_time = time()
        self.cost = 0.

    def _hire_editor(self) -> Assistant:
        assistant = Assistant(definition="You are a creative AI assistant", name='')
        task = dedent(
            """
            I need to hire an Editor-in-Chief for a daily tech magazine. Think of 4 different types
            of editors and describe their characteristics.
            Your response should be a JSON, where the keys are the names of the editors (which you generate),
            and the values are their characteristics description.
            Follow this schema:
            ```json
            {"FULL NAME": "DESCRIPTION", ...}
            ```
            For example:
            ```json
            {"John Smith": "You are a ..."}
            ```
            IMPORTANT: Describe their characteristics as if you are talking to each one of them, in second body.
            """.strip())
        result = assistant.do(task, as_json=True)
        self.cost += result['cost']
        possible_editors = [{'name': k, 'definition': v} for k,v in json.loads(result['response']).items()]
        self.logger.debug(possible_editors)
        selected_editor = possible_editors[randint(0,3)]
        return Assistant(definition=selected_editor['definition'], name=selected_editor['name'])
    
    def _hire_reporters(self) -> list[Assistant]:
        task = dedent(
            f"""
            You must hire {self.NUM_OF_REPORTERS} reporters to research, choose and write the articles
            for today's issue about the latest news and trends in tech and AI. 
            Describe each of the {self.NUM_OF_REPORTERS} individuals you hire for this task.
            Your response should be a JSON, where the keys are the names of the reporters (which you generate),
            and the values are their characteristics description.
            IMPORTANT: Describe their characteristics as if you are talking to each one of them, in second body.
            """.strip())
        result = self.editor.do(task, as_json=True)
        self.cost += result['cost']
        self.logger.debug(result['response'])
        reporters = []
        for name, description in list(json.loads(result['response']).items())[:self.NUM_OF_REPORTERS]:
            reporters.append(Assistant(description, name=name))
        return reporters
    
    def _research(self, items_per_reporter: int = 5) -> list[dict[str, str]]:
        editor_task = dedent(
            f"""
            Brief your staff about the type of news you'd like them to look for for today's issue.
            Explain to them what you're expecting of them. Here are some example topics:
            {self.TOPICS}
            Feel free to edit, add or remove topics as you wish. You may also look on the web for new ideas.
            Reply as if you speak to your reporters directly.
            """)
        editor_response = self.editor.do(editor_task)
        self.cost += editor_response['cost']
        guidelines = dedent(
            f"""
            IMPORTANT GUIDELINES:
            - Search the web and read webpages to complete your assignment. Make as many searches as required
            - You must provide AT LEAST {items_per_reporter} items
            - Your response should be formatted as JSON, where the items titles (meaning: the titles of the 
              articles you read) are the keys, and the values are the items URLs.
              Example:
            ```json
            {{"OpenAI's Sora text-to-video generator will be publicly available later this year": "https://www.theverge.com/2024/3/13/24099402/openai-text-to-video-ai-sora-public-availability"}}
            ```
            """.strip())
        reporters_task = editor_response['response'] + '\n' + guidelines
        self.logger.debug(reporters_task)
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(reporter.do, reporters_task, as_json=True) for reporter in self.reporters]
        results = [f.result() for f in futures]
        self.cost += sum([r['cost'] for r in results])
        self.logger.debug([r['response'] for r in results])
        return [json.loads(r['response']) for r in results]
    
    def _select_items(self, suggestions: list[dict[str, str]], num_items: int = 7) -> dict[str, dict[str, Any]]:
        _l = flatten([[{'title': k, 'url': v} for k,v in s.items()] for s in suggestions])
        suggestions_text = '\n'.join([f'* {d["title"]} | URL: {d["url"]}' for d in _l])
        task = dedent(
            f"""
            The list below contains the items suggestions provided by your staff:
            {suggestions_text}
            Your task is to select the top {num_items} from this list to be featured in today's issue.
            Note that as your reporters worked independently, some suggestions might be duplicates (either
            same topic from different sources or even the exact same item). Make sure to select {num_items} DIFFERENT
            items of different topics. Rank your selection from 1 to {num_items}, where 1 is the top item of today's issue.
            Return your selection as JSON, where the item title is the key, and the value is another dictionary, holding
            your chosen rank and a list of similar items to that item, if any. See the example below:
            ```json
            {{"ITEM_TITLE": 
                {{
                    "rank": int_value,
                    "similar": ["TITLE_OF_SIMILAR_ITEMS", ...]  // keep empty if none
                }}
            }}
            ```
            """.strip())
        result = self.editor.do(task, as_json=True)
        self.cost += result['cost']
        self.logger.debug(result['response'])
        return json.loads(result['response'])
    
    def _write_items(self, items: list[list[dict[str, str]]]) -> dict[str, str]:
        # Each input item is {'title': title, 'url': url}
        error_message = "<ERROR>"
        articles: dict[str, str] = {}
        task = dedent(
            """
            Write a summary for toady's issue on {title} (URL: {url}). 
            Follow these guidelines:
            - It should be no more than 200 words
            - Do NOT add a title, the editor will add it later
            - Your response is printed as it is, so do not add any other remarks beside the summary

            IMPORTANT: If you encounter an error or an issue completing this task, simple respond with "{error}".
            """)
        
        def reporter_tasks(reporter: Assistant, reporter_items: list[dict[str, str]]):  
            for item in reporter_items:
                result = reporter.do(task.format(title=item['title'], url=item['url'], error=error_message))
                self.cost += result['cost']
                if not error_message in result['response']:
                    articles[item['title']] = result['response']
        
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(reporter_tasks, reporter, reporter_items) for reporter, reporter_items in zip(self.reporters, items)]
        [f.result() for f in futures]
        self.logger.debug(articles)
        return articles

    def _get_elapsed_time(self) -> str:
        elapsed_time = time() - self.start_time
        delta = timedelta(minutes=elapsed_time//60, seconds=elapsed_time%60)
        return str(delta)

    def do(self) -> None:
        self.start_time = time()
        self.cost = 0.

        self.logger.info("Starting - Hiring editor", color='green')
        self.editor =  self._hire_editor()
        
        self.logger.info(f"Hiring staff [elapsed time: {self._get_elapsed_time()}, cost: {round(self.cost, 2)}$]", color='green')
        self.reporters = self._hire_reporters()
        
        self.logger.info(f"Performing research [elapsed time: {self._get_elapsed_time()}, cost: {round(self.cost, 2)}$]", color='green')
        suggestions = self._research()  # index of list is the index of reporter, dicts are {title: url}

        self.logger.info(f"Selecting top items [elapsed time: {self._get_elapsed_time()}, cost: {round(self.cost, 2)}$]", color='green')
        selected_items = self._select_items(suggestions) # dict {title: {rank: i, similar: []}}
        items_for_reporters: list[list[dict[str, str]]] = [[] for x in [None] * self.NUM_OF_REPORTERS if x is None]
        for title in selected_items.keys():
            reporter_index = next((suggestions.index(s) for s in suggestions if title in s.keys()), -1)
            url = suggestions[reporter_index][title]
            items_for_reporters[reporter_index].append({'title': title, 'url': url})
        
        self.logger.info(f"Writing articles [elapsed time: {self._get_elapsed_time()}, cost: {round(self.cost, 2)}$]", color='green')
        articles_dict = self._write_items(items_for_reporters)
        articles = [(title, text) for title, text in articles_dict.items()]
        articles = sorted(articles, key=lambda tup: selected_items[tup[0]]['rank'])
        md_articles = []
        for title, text in articles:
            reporter_index = next((suggestions.index(s) for s in suggestions if title in s.keys()), -1)
            md_articles.append(f"# {title}\n_By: {self.reporters[reporter_index].name}_ [[link]({suggestions[reporter_index][title]})]\n\n{text}")
        with open(f'{datetime.now().strftime("%Y-%m-%d")}-news.md', 'w') as f:
            f.write('\n\n'.join(md_articles))
        self.logger.info(f"Done. [total elapsed time: {self._get_elapsed_time()}, total cost: {round(self.cost, 2)}$]", color='green')
        