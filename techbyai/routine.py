import json
from time import time
from datetime import datetime, timedelta
from random import randint, shuffle
from textwrap import dedent
from concurrent.futures import ThreadPoolExecutor
from typing import Any
from .assistant import Assistant
from .item_suggestion import ItemSuggestion
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
        self.logger.debug(f"Selected editor: {selected_editor['name']} - {selected_editor['definition']}")
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
    
    def _research(self, items_per_reporter: int = 5) -> list[list[ItemSuggestion]]:
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
            REMEMBER: You are competing with the rest of the staff on finding the most interesting items, so be
            creative in your searches, don't just copy paste the editor's instructions!
            """.strip())
        reporters_task = editor_response['response'] + '\n' + guidelines
        self.logger.debug(reporters_task)
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(reporter.do, reporters_task, as_json=True) for reporter in self.reporters]
        results = [f.result() for f in futures]
        self.cost += sum([r['cost'] for r in results])
        self.logger.debug([r['response'] for r in results])
        suggestions: list[list[ItemSuggestion]] = []
        for i, reporter_suggestions_dict in enumerate([json.loads(r['response']) for r in results]):
            reporter_suggestions: list[ItemSuggestion] = []
            for title, url in reporter_suggestions_dict.items():
                reporter_suggestions.append(ItemSuggestion(title=title, url=url, reporter=self.reporters[i].name))
            suggestions.append(reporter_suggestions)
        return suggestions
    
    def _select_items(self, suggestions: list[list[ItemSuggestion]], num_items: int = 7) -> list[list[ItemSuggestion]]:
        suggestions_text = '\n'.join([f'* {s.title} (URL: {s.url}) | Item ID: {s.id}' for s in flatten(suggestions)])
        task = dedent(
            f"""
            The list below contains the items suggestions provided by your staff:
            {suggestions_text}
            Your task is to select the top {num_items} from this list to be featured in today's issue.
            Note that as your reporters worked independently, some suggestions might be duplicates (either
            same topic from different sources or even the exact same item). Make sure to select {num_items} DIFFERENT
            items of different topics. Rank your selection from 1 to {num_items}, where 1 is the top item of today's issue.
            Return your selection as JSON, where the item ID is the key, and the value is another dictionary, holding
            your chosen rank and a list of similar item IDs to that item, if any. See the example below:
            ```json
            {{"ITEM_ID": 
                {{
                    "rank": int_value,
                    "similar": ["ID_OF_SIMILAR_ITEMS", ...]  // keep empty if none
                }}
            }}
            ```
            """.strip())
        result = self.editor.do(task, as_json=True)
        self.cost += result['cost']
        self.logger.debug(result['response'])
        ranking = json.loads(result['response'])
        for s_id, dct in ranking.items():
            indices = list(range(len(suggestions)))
            shuffle(indices)
            for i in indices:
                reporter_suggestions = suggestions[i]
                reporter_s_ids = [sg.id for sg in reporter_suggestions]
                if s_id in reporter_s_ids:
                    idx = reporter_s_ids.index(s_id)
                    suggestion = reporter_suggestions[idx]
                    suggestion.rank = int(dct['rank'])
                    suggestion.similar_ids = dct.get('similar', [])
                    reporter_suggestions[idx] = suggestion
                    break
        return suggestions
    
    def _write_items(self, items: list[list[ItemSuggestion]]) -> list[list[ItemSuggestion]]:
        error_message = "<ERROR>"
        task = dedent(
            """
            Write a summary for toady's issue on {title} (URL: {url}). 
            Follow these guidelines:
            - It should be no more than 200 words
            - Do NOT add a title, the editor will add it later
            - Your response is printed as it is, so do not add any other remarks beside the summary
            - Use Markdown syntax

            IMPORTANT: If you encounter an error or an issue completing this task, simple respond with "{error}".
            """)
        
        def reporter_tasks(reporter: Assistant, reporter_items: list[ItemSuggestion]) -> list[ItemSuggestion]:  
            for i, item in enumerate(reporter_items):
                if item.rank < 0:
                    continue
                result = reporter.do(task.format(title=item.title, url=item.url, error=error_message))
                self.cost += result['cost']
                if not error_message in result['response']:
                    item.text = result['response']
                else:
                    item.rank = -1
                reporter_items[i] = item
            return reporter_items
        
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(reporter_tasks, reporter, reporter_items) for reporter, reporter_items in zip(self.reporters, items)]
        items_with_text = [f.result() for f in futures]
        self.logger.debug('\n\n'.join(s.text for s in flatten(items_with_text) if s.text))
        return items_with_text

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
        suggestions = self._research() 

        self.logger.info(f"Selecting top items [elapsed time: {self._get_elapsed_time()}, cost: {round(self.cost, 2)}$]", color='green')
        suggestions = self._select_items(suggestions) 
        
        self.logger.info(f"Writing articles [elapsed time: {self._get_elapsed_time()}, cost: {round(self.cost, 2)}$]", color='green')
        items = flatten(self._write_items(suggestions))
        items = sorted(items, key=lambda s: s.rank if s.rank > 0 else 999)
        md_ranked_articles = []
        md_unranked_articles = []
        ranked_ids = [item.id for item in items if item.rank > 0]
        for item in items:
            if item.rank == -1: 
                    if item.id not in ranked_ids:
                        md_unranked_articles.append(f'* [{item.title}]({item.url})')
            else:
                md_ranked_articles.append(f"# {item.title}\n_Summarized by: {item.reporter}_ [[link]({item.url})]\n\n{item.text}")
        with open(f'{datetime.now().strftime("%Y-%m-%d")}-news.md', 'w') as f:
            f.write('\n\n'.join(md_ranked_articles))
            f.write('\n\n**Other headlines:**\n')
            f.write('\n'.join(md_unranked_articles))
        self.logger.info(f"Done. [total elapsed time: {self._get_elapsed_time()}, total cost: {round(self.cost, 2)}$]", color='green')
        