import re
import os
import pathlib
from time import time
from datetime import datetime, timedelta
from random import randint, shuffle
from textwrap import dedent
from concurrent.futures import ThreadPoolExecutor
from .assistant import Assistant
from .item_suggestion import ItemSuggestion
from .color_logger import get_logger
from .utils import flatten, domain_of_url, get_version, path_to_resource
from .settings import Settings
from .cost import Cost
from .audio import Narrator


class Routine:
    def __init__(self) -> None:
        self.editor: Assistant
        self.reporters: list[Assistant] = []
        self.logger = get_logger()
        self.start_time = time()
        self.cost = Cost()
        self.narrator = Narrator()

    @property
    def topics(self) -> str:
        companies: list[str] = Settings().editorial.companies
        people: list[str] = Settings().editorial.people
        topics_list: list[str] = Settings().editorial.topics
        if companies:
            shuffle(companies)
            topics_list.append(f"Companies such as: {' '.join(companies)}")
        if people:
            shuffle(people)
            topics_list.append(f"News, projects and interesting tweets coming from top-minds like these: {' '.join(people)}")
        shuffle(topics_list)
        return ", ".join(topics_list)

    def _hire_editor(self) -> Assistant:
        assistant = Assistant(definition="You are a creative AI assistant", name='')
        task = dedent(
            f"""
            I need to hire an Editor-in-Chief for a daily {Settings().editorial.subject} magazine. Think of 4 different types
            of editors and describe their characteristics.
            Your response should be a JSON, where the keys are the names of the editors (which you generate),
            and the values are their characteristics description.
            Follow this schema:
            ```json
            {{"FULL NAME": "DESCRIPTION", ...}}
            ```
            For example:
            ```json
            {{"John Smith": "You are a ..."}}
            ```
            IMPORTANT: Describe their characteristics as if you are talking to each one of them, in second body.
            """.strip())
        result = assistant.do(task, as_json=True)
        possible_editors = [{'name': k, 'definition': v} for k,v in result.json.items()]
        self.logger.debug(possible_editors)
        selected_editor = possible_editors[randint(0,3)]
        self.logger.debug(f"Selected editor: {selected_editor['name']} - {selected_editor['definition']}")
        editor_def = f"You are the Editor-in-Chief of a daily {Settings().editorial.subject} magazine named \"{Settings().editorial.name}\". {selected_editor['definition']}"
        return Assistant(definition=editor_def, name=selected_editor['name'])
    
    def _hire_reporters(self) -> list[Assistant]:
        task = dedent(
            f"""
            You must hire {Settings().editorial.reporters} reporters to research, choose and write the articles
            for today's issue about the latest news and trends in {Settings().editorial.subject}. 
            Describe each of the {Settings().editorial.reporters} individuals you hire for this task.
            Your response should be a JSON, where the keys are the names of the reporters (which you generate),
            and the values are their characteristics description.
            IMPORTANT: Describe their characteristics as if you are talking to each one of them, in second body.
            """.strip())
        result = self.editor.do(task, as_json=True)
        self.logger.debug(result.content)
        reporters = []
        for name, description in list(result.json.items())[:Settings().editorial.reporters]:
            reporters.append(Assistant(description, name=name))
        return reporters
    
    def _research(self) -> list[list[ItemSuggestion]]:
        editor_task = dedent(
            f"""
            Brief your staff about the type of news you'd like them to look for for today's issue.
            Explain to them what you're expecting of them. Here are some example topics:
            {self.topics}
            Feel free to edit, add or remove topics as you wish. You may also look on the web for new ideas.
            Reply as if you speak to your reporters directly.
            """)
        editor_response = self.editor.do(editor_task)
        guidelines = dedent(
            f"""
            IMPORTANT GUIDELINES:
            - Come up with at least {2*Settings().editorial.reporter_items} DIFFERENT search queries. 
              For each query, search the web and read webpages to complete your assignment
            - You must provide AT LEAST {Settings().editorial.reporter_items} items
            - The readers of the magazine are professionals, AVOID articles about broad reviews of topics and trends, focus and actual novelties, breakthroughs and updates
            - If the title you got from the search ends with "...", visit the website and extract the full title from there
            - Make sure the URL you provide direct to the exact article you chose (and not to a some news aggregation). Search for the specific URL of the article if needed
            - Your response should be formatted as JSON, where the items titles (meaning: the titles of the 
              articles you read) are the keys, and the values are the items URLs.
              Example:
            ```json
            {{"OpenAI's Sora text-to-video generator will be publicly available later this year": "https://www.theverge.com/2024/3/13/24099402/openai-text-to-video-ai-sora-public-availability"}}
            ```
            REMEMBER: You are competing with the rest of the staff on finding the most interesting items, so be
            creative in your searches, don't just copy paste the editor's instructions!
            """.strip())
        reporters_task = editor_response.content + '\n' + guidelines
        self.logger.debug(reporters_task)
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(reporter.do, reporters_task, as_json=True) for reporter in self.reporters]
        results = [f.result() for f in futures]
        self.logger.debug([r.content for r in results])
        suggestions: list[list[ItemSuggestion]] = []
        for i, reporter_suggestions_dict in enumerate([r.json for r in results]):
            reporter_suggestions: list[ItemSuggestion] = []
            for title, url in reporter_suggestions_dict.items():
                reporter_suggestions.append(ItemSuggestion(title=title, url=url, reporter=self.reporters[i].name))
            suggestions.append(reporter_suggestions)
        return suggestions
    
    def _select_items(self, suggestions: list[list[ItemSuggestion]]) -> list[list[ItemSuggestion]]:
        suggestions_text = '\n'.join([f'* {s.title} (URL: {s.url}) | Item ID: {s.id}' for s in flatten(suggestions)])
        task = dedent(
            f"""
            The list below contains the items suggestions provided by your staff:
            {suggestions_text}
            Your task is to select the top ~{Settings().editorial.final_items} (but no less than {Settings().editorial.final_items - 2}) from this list to be featured in today's issue.
            Note that as your reporters worked independently, some suggestions might be duplicates (either
            same topic from different sources or even the exact same item). Make sure to select {Settings().editorial.final_items} DIFFERENT
            items of different topics. Rank your selection from 1 to {Settings().editorial.final_items}, where 1 is the top item of today's issue.
            Return your selection as JSON, where the item ID is the key, and the value is another dictionary, holding
            your chosen rank and a list of similar item IDs to that item, if any. 
            See the example below:
            ```json
            {{"ITEM_ID": 
                {{
                    "rank": int_value,
                    "similar": ["ID_OF_SIMILAR_ITEMS", ...]  // keep empty if none
                }}
            }}
            ```
            Guidelines:
            - Never rank two items which are considered similar! Choose your favorite, list the rest under the `similar` list.
            - You MUST READ the article, and VERIFY it refers to events, news or updates from the past 2 days - do NOT rank article which discuss older news or topics!
            - REFRAIN from having promotional content on your magazine. 
              If you're using content shared by the same company or person who created it, make sure it actually professionally valuable, and simply self-endorsing.
              Verify the article really has valuable information which will enrich the readers!
            - The readers of the magazine are professionals, AVOID articles about broad reviews of topics and trends, focus and actual novelties, breakthroughs and updates
            REMEMBER: You are being assessed by the quality of the content of your magazine, make sure to make it as 
            interesting and professional as possible!
            """.strip())
        result = self.editor.do(task, as_json=True)
        self.logger.debug(result.content)
        ranking = result.json
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
        remove_message = "<REMOVE>"
        
        def editor_task(text: str) -> str:
            task = dedent(
                f"""
                The text below is the final article written by one of your reporters.
                Review it, and edit it if you fell it is necessary in order for it to meet your magazine's guidelines.
                Still, try to intervene as les as possible, if at all. Do so only if you find it to be necessary.
                Also, you have the option not to use this article in you magazine, if you believe it does not mee your standards
                or will have no value to your professional readers. 
                - If you choose to remove this article, reply only with {remove_message}
                - If you wish to keep it, reply only with the final version of your edited version. Remember it must not exceed {Settings().editorial.max_words_per_item}!
                  Also, your response will be used as it is, so do not add any other remarks but the text. 
                - If you choose not to edit the text at all, copy the text as it is, word for word
                """)
            result = self.editor.do(f"{task}\n---\n{text}")
            return result.content
        
        def reporter_tasks(reporter: Assistant, reporter_items: list[ItemSuggestion]) -> list[ItemSuggestion]:  
            for i, item in enumerate(reporter_items):
                if item.rank < 0:
                    continue

                task = dedent(
                    f"""
                    Write a summary for toady's issue on {item.title} (URL: {item.url}). 
                    Follow these guidelines:
                    - It should be no more than {Settings().editorial.max_words_per_item} words
                    - Do NOT add a title, the editor will add it later
                    - Your response is printed as it is, so do not add any other remarks beside the summary
                    - Use Markdown syntax

                    IMPORTANT: If you encounter an error or an issue completing this task, simple respond with "{error_message}".
                    """)
                result = reporter.do(task)
                if not error_message in result.content:
                    text = result.content
                    edited_text = editor_task(text)
                    if remove_message in edited_text:
                        item.rank = -1
                    else:
                        item.text = edited_text
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
    
    def _create_title_and_subtitle(self, full_article: str) -> dict[str, str]:
        task = dedent(
            f"""
            The text below is the full article to be published today in your magazine:
            ---
            {full_article}
            ---
            Write a title and subtitle for it. Title should be up to 10 words, and subtitle up to 20 words.
            Remember your magazine is a DAILY magazine, so make sure the title isn't about the whole month or year.
            Also, make it sound professional, not amateur.
            Return your response as JSON in the format below:
            ```json
            {{
                "title": "YOUR TITLE",
                "subtitle": "YOUR SUBTITLE
            }}
            ```
            """.strip())
        result = self.editor.do(task, as_json=True)
        return result.json
    
    def _write_markdown_article(self, items: list[ItemSuggestion]) -> str:
        items = sorted(items, key=lambda s: s.rank if s.rank > 0 else 999)
        md_ranked_articles = []
        md_unranked_articles = []
        ranked_ids = [item.id for item in items if item.rank > 0]
        ids_of_written = []
        for item in items:
            if item.id in ids_of_written:
                continue
            
            if item.rank == -1: 
                if item.id not in ranked_ids:
                    u = item.url.split("://")[-1]
                    if u.endswith("/"): 
                        u = u[:-1]
                    if u != domain_of_url(item.url):
                        md_unranked_articles.append(f'* [{item.title.replace(" | ", " ").replace("|", " ")}]({item.url})')
            else:
                similar_items = []
                for s_id in item.similar_ids:
                    sim_list = [im for im in items if im.id == s_id]
                    if len(sim_list) == 0:
                        continue
                    sim = sim_list[0]
                    if domain_of_url(sim.url) == domain_of_url(item.url):
                        continue
                    similar_items.append(f'> * [{sim.title.replace(" | ", " ").replace("|", " ")}]({sim.url}) ({domain_of_url(sim.url)})')
                    ids_of_written.append(sim.id)
                if similar_items:
                    similar_items = ["\n> **See also:**"] + similar_items
                similar_text = '\n'.join(similar_items)
                domain = domain_of_url(item.url)
                md_ranked_articles.append(f"# {item.title}\n_Summarized by: {item.reporter}_ [[{domain}]({item.url})]{similar_text}\n\n{item.text}")
            ids_of_written.append(item.id)


        self.logger.info(f"Creating title for article [elapsed time: {self._get_elapsed_time()}, cost: {self.cost()}$]", color='green')
        
        self.logger.info(f"Creating title for article [elapsed time: {self._get_elapsed_time()}, cost: {self.cost()}$]", color='green')
        full_article = '\n\n'.join(md_ranked_articles) + '\n\n**Other headlines:**\n' + '\n'.join(md_unranked_articles)
        return full_article

    @property
    def output_dir(self) -> str:
        top_dir = pathlib.Path(__file__).parent.parent.resolve()
        output_dir = os.path.join(top_dir, "results")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        return output_dir
    
    def _markdown_metadata(self, title: str, subtitle: str, audio_filename: str, audio_filepath: str, audio_duration: str) -> str:
        metadata = dedent(
            f"""
            ---
            layout: post
            title: "{title}"
            subtitle: "{subtitle}"
            audio: {audio_filename}
            date: {datetime.now().strftime("%Y-%m-%d")}
            duration: "{audio_duration}"
            bytes: {os.path.getsize(audio_filepath)}
            model: {Settings().llm.model}
            cost: {self.cost()}
            processing: "{self._get_elapsed_time()}"
            version: "{get_version()}"
            ---
            """.strip())
        return '\n'.join(s.lstrip() for s in metadata.split('\n'))

    def do(self) -> None:
        self.cost.reset()
        self.start_time = time()

        self.logger.info("Starting - Hiring editor", color='green')
        self.editor =  self._hire_editor()
        
        self.logger.info(f"Hiring staff [elapsed time: {self._get_elapsed_time()}, cost: {self.cost()}$]", color='green')
        self.reporters = self._hire_reporters()
        
        self.logger.info(f"Performing research [elapsed time: {self._get_elapsed_time()}, cost: {self.cost()}$]", color='green')
        suggestions = self._research() 

        self.logger.info(f"Selecting top items [elapsed time: {self._get_elapsed_time()}, cost: {self.cost()}$]", color='green')
        suggestions = self._select_items(suggestions) 
        
        self.logger.info(f"Writing articles [elapsed time: {self._get_elapsed_time()}, cost: {self.cost()}$]", color='green')
        items = flatten(self._write_items(suggestions))
        
        self.logger.info(f"Composing article [elapsed time: {self._get_elapsed_time()}, cost: {self.cost()}$]", color='green')
        full_article = self._write_markdown_article(items)
        title_and_subtitle = self._create_title_and_subtitle(full_article)
        title_and_subtitle['title'] = title_and_subtitle['title'] or f'AI News: {datetime.now().strftime("%A, %d %B, %Y")}'
        title_and_subtitle['subtitle'] = title_and_subtitle['subtitle'] or "All the latest news about AI, brought to you by AI"

        alphanumeric_title = re.sub(r'[^A-Za-z0-9 ]+', '', title_and_subtitle["title"])
        filename = f'{datetime.now().strftime("%Y-%m-%d")}-{alphanumeric_title.lower().replace(" ","-")}'

        self.logger.info(f"Narrating [elapsed time: {self._get_elapsed_time()}, cost: {self.cost()}$]", color='green')
        recording_filepath = os.path.join(self.output_dir, filename+'.mp3')
        output_audio = self.narrator.narrate(items, title=title_and_subtitle['title'])
        length_seconds = int(len(output_audio) / 1000)
        output_audio.export(recording_filepath, format="mp3")

        minutes, seconds = divmod(length_seconds, 60)
        duration_str = "{:02d}:{:02d}".format(int(minutes), int(seconds))

        filepath = os.path.join(self.output_dir, filename+'.md')
        with open(filepath, 'w') as f:
            f.write(self._markdown_metadata(title=title_and_subtitle['title'], subtitle=title_and_subtitle['subtitle'], audio_filename=filename+".mp3", audio_filepath=recording_filepath, audio_duration=duration_str) + '\n\n')
            f.write(full_article + '\n\n')  
            f.write(f'---\n### Technical details\nCreated at: {datetime.now().strftime("%d %B, %Y, %H:%M:%S")}, ' + 'using `{{ page.model }}`.\n\nProcessing time: {{ page.processing }}, cost: {{ page.cost }}$\n')
            f.write(f'<details>\n<summary>The Staff</summary>\n<div markdown="1">\nEditor: {self.editor.name}\n\n```\n{self.editor.definition}\n```\n\n')
            f.write('\n\n'.join([f'{reporter.name}:\n\n```\n{reporter.definition}\n```' for reporter in self.reporters]))
            f.write("\n</div>\n</details>\n")
        
        self.logger.info(f"Done. [total elapsed time: {self._get_elapsed_time()}, total cost: {self.cost()}$]", color='green')
        