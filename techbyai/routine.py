import re
import os
import pathlib
import pandas as pd
from time import time
from datetime import datetime, timedelta
from random import randint, shuffle
from textwrap import dedent
from concurrent.futures import ThreadPoolExecutor
from .assistant import Assistant
from .item_suggestion import ItemSuggestion
from .color_logger import get_logger
from .utils import flatten, domain_of_url, get_version
from .settings import Settings
from .cost import Cost
from .audio import Narrator
from .archive import Archive, Embedder
from .viewed_urls import ViewedURLs
from .tools import WEB_TOOLS, ARXIV_TOOLS, TWITTER_TOOLS, MAGAZINE_TOOLS


class Routine:
    def __init__(self) -> None:
        """
        Initializes the `Editor`, providing an assistant, a list of analysts, a
        logger, and various counters for tracking time, cost, and viewed URLs.

        """
        self.editor: Assistant
        self.twitter_analyst: Assistant
        self.reporters: list[Assistant] = []
        self.logger = get_logger()
        self.start_time = time()
        self.cost = Cost()
        self.archive = Archive()
        self.viewed_urls = ViewedURLs()

    def topics(self, twitter_trends: list[str]) -> str:
        """
        Generates a list of editorial topics based on user-provided input. It takes
        two lists as inputs: `companies`, which are shuffled and concatenated into
        a single string, and `twitter_trends`, which are also shuffled and appended
        to the list of topics. The function then returns a joined list of all the
        topics.

        Args:
            twitter_trends (list[str]): 5-10 trending topics on Twitter that will
                be added to the list of topics to be joined with the companies' names.

        Returns:
            str: a list of random topics, either generated from a list of companies
            or from Twitter trends.

        """
        companies: list[str] = Settings().editorial.companies
        topics_list: list[str] = Settings().editorial.topics
        if companies:
            shuffle(companies)
            topics_list.append(f"Companies such as: {', '.join(companies)}")
        if twitter_trends:
            shuffle(twitter_trends)
            topics_list.append(f"These trending topics on Twitter: {', '.join(twitter_trends)}")
        shuffle(topics_list)
        return ", ".join(topics_list)

    def _hire_editor(self) -> Assistant:
        """
        Creates an Assistant with customized definition, name, and tools based on
        user input. It generates possible editor names and descriptions using a
        random pick from predefined options, then selects and returns the selected
        editor's information as an Assistant instance.

        Returns:
            Assistant: an Assistant object with a custom definition, name, and tools.

        """
        num_editors = 3
        assistant = Assistant(definition="You are a creative AI assistant")
        task = dedent(
            f"""
            I need to hire an Editor-in-Chief for a daily {Settings().editorial.subject} magazine. Think of {num_editors} different types
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
            Be original with the names you choose, but don't go silly.
            IMPORTANT: Describe their characteristics as if you are talking to each one of them, in second body.
            """.strip())
        result = assistant.do(task, as_json=True)
        possible_editors = [{'name': k, 'definition': v} for k,v in result.json.items()]
        self.logger.debug(possible_editors)
        selected_editor = possible_editors[randint(0, num_editors-1)]
        self.logger.debug(f"Selected editor: {selected_editor['name']} - {selected_editor['definition']}")
        editor_def = f"You are the Editor-in-Chief of a daily {Settings().editorial.subject} magazine named \"{Settings().editorial.name}\". {selected_editor['definition']}"
        return Assistant(definition=editor_def, name=selected_editor['name'], archive=self.archive, tools=WEB_TOOLS + ARXIV_TOOLS + TWITTER_TOOLS + MAGAZINE_TOOLS)
    
    def _hire_reporters(self) -> tuple[list[Assistant], Assistant]:
        """
        Takes a task as input, which is a JSON object with characteristics of each
        reporter to be hired for a daily magazine issue. The function returns a
        list of Assistant instances representing the hired reporters and a single
        Twitter analyst, along with their respective tools.

        Returns:
            tuple[list[Assistant], Assistant]: a list of `Assistant` objects, each
            representing a reporter or analyst for a daily magazine.

        """
        task = dedent(
            f"""
            You must hire {Settings().editorial.reporters} reporters to research, choose and write the articles
            for today's issue about the latest news and trends in {Settings().editorial.subject}. 
            Describe each of the {Settings().editorial.reporters} individuals you hire for this task. 
            Your response should be a JSON, where the keys are the names of the reporters (which you generate),
            and the values are their characteristics description. Don't write the description as a JSON too, but as a coherent and fluent text (i.e. "You are...")
            Be creative with the names you choose, but don't go silly.
            IMPORTANT: Describe their characteristics as if you are talking to each one of them, in second body.
            """.strip())
        result = self.editor.do(task, as_json=True)
        self.logger.debug(result.content)
        reporters_kv_list = list(result.json.items())[:Settings().editorial.reporters]
        reporters = []
        for i, (name, description) in enumerate(reporters_kv_list):
            reporter_def = f"You are a reporter of a daily {Settings().editorial.subject} magazine named \"{Settings().editorial.name}\". {description}"
            tools = ARXIV_TOOLS if i == 0 else WEB_TOOLS
            reporters.append(Assistant(reporter_def, name=name, tools=tools))
        
        second_task = dedent(
            f"""
            You must hire a single Twitter savvy as part of your staff. This person is an analyst, the one who knows how to find the most interesting and trending information on Twitter,
            and do research for topics to write about.
            Describe this individual. 
            Your response should be a JSON, where the keys are the names of the reporters (which you generate),
            Don't write the description as a JSON too, but as a coherent and fluent text (i.e. "You are...")
            and the values are their characteristics description. The name should be different than the names of your other reporters: {list(result.json.keys())}.
            IMPORTANT: Describe their characteristics as if you are talking to each one of them, in second body.
            """.strip())
        result = self.editor.do(second_task, as_json=True)
        self.logger.debug(result.content)
        for name, description in list(result.json.items())[:1]:
            analyst_def = f"You are a Twitter analyst, working for a daily {Settings().editorial.subject} magazine named \"{Settings().editorial.name}\". {description}"
            twitter_savvy = Assistant(analyst_def, name=name, tools=TWITTER_TOOLS + WEB_TOOLS)
        return reporters, twitter_savvy
    
    def _twitter_analysis(self) -> tuple[list[str], list[int]]:
        """
        1) generates a list of people and influencers to follow on Twitter for a
        specific field, and 2) searches Twitter for interesting and trending topics
        discussed by those individuals, selecting up to `Settings().editorial.reporter_items`
        topics with associated tweets.

        Returns:
            tuple[list[str], list[int]]: a list of trending topics on Twitter and
            the corresponding tweets.

        """
        initial_task = dedent(
            f"""
            Come up with a list of people and influencers in the fields of {Settings().editorial.subject} which should be followed on Twitter.
            Return your list as a JSON, of the following format:
            ```json
            {{"USERNAME": "FULL NAME", ...}}
            ```
            Where USERNAME is the Twitter user-name (user-handle) of the person.
            Be creative in your selection, but always choose people who are considered credible and reliable in their fields!
            """.strip())
        result = self.twitter_analyst.do(initial_task, as_json=True)
        self.logger.debug(result.content)
        predefined_twitter_accounts: dict[str, str] = Settings().editorial.twitter_accounts
        accounts: dict[str, str] = {k.strip('@'): v for k,v in result.json.items()}
        people: dict[str, str] = accounts | predefined_twitter_accounts
        self.logger.info(f"Following these people on Twitter: {[f'{v} (@{k})' for k,v in people.items()]}")
        people_as_list = '\n'.join([f'* {v} (username: {k})' for k,v in people.items()])

        second_task = dedent(
            f"""
            Search on Twitter for the most interesting and trending topics these people and influencers discuss in the fields of {Settings().editorial.subject}:
            {people_as_list}
            Choose up to {Settings().editorial.reporter_items} topics based on their tweets, along with ~2 tweets per topic (the best ones by your opinion), 
            and return your decision as a JSON in the following format:
            ```json
            {{
                "topics": ["SPECIFIC_TOPIC", ...],
                "tweets": [URL_ID, ...]  // this should be a list of IDs of tweets by some of the people mentioned above about this topic
            }}
            IMPORTANT: 
            - Do NOT choose broad topics (i.e. "Ethics and Bias in AI", "Advancements in Natural Language Processing", and things like that)! Choose very 
              specific subjects (a new model, a new breakthrough, etc.) Prefer less topics than broad topics!
            - Search for tweets using the `search_for_tweets` tool. Remember the `query` parameter is optional! Give it a go without a query first, and use it to filter results
            - DO NOT, and I repeat - DO NOT use tweets of random users, as they might be spam. You are only allowed to use tweets posted by the people on the list!
            - Prefer to list tweets from as many different people from those provided. DO NOT choose more than a single tweet per user!
            - DO NOT BE LAZY! If one search didn't yield result, try another! Don't stop trying before truing 5 different attempts!
            ```
            """.strip())
        result = self.twitter_analyst.do(second_task, as_json=True)
        self.logger.debug(result.content)
        trends: list[str] = result.json.get('topics', [])
        tweets: list[int] = [int(v) for v in result.json.get('tweets', [])]
        self.logger.debug(f"Twitter trends: {trends}")
        return trends, tweets
    
    def _research(self, twitter_trends: list[str]) -> list[list[ItemSuggestion]]:
        """
        Takes in a list of editors and tasks them with researching for code news
        and providing their findings as a JSON response.

        Args:
            twitter_trends (list[str]): 2D array of topics to look for in news
                articles, which are automatically generated based on recent trending
                Twitter topics.

        Returns:
            list[list[ItemSuggestion]]: a list of lists, where each inner list
            contains item suggestions from the reporters based on their research.

        """
        editor_task = dedent(
            f"""
            Brief your staff about the type of news you'd like them to look for for today's issue.
            Explain to them what you're expecting of them. Here are some example topics:
            {self.topics(twitter_trends)}
            Feel free to edit, add or remove topics as you wish. You may also look on the web for new ideas.
            Reply as if you speak to your reporters directly.
            """)
        editor_response = self.editor.do(editor_task)
        guidelines = dedent(
            f"""
            ---
            IMPORTANT GUIDELINES:
            - Come up with at least {2*Settings().editorial.reporter_items} DIFFERENT search queries. 
              For each query, search the web and read webpages to complete your assignment
            - Consider the credibility and reliability of the sources you choose 
            - Titles dont tend to end with '...' (three-dots). If it does, get the page content and get the title from it!
            - You must provide AT LEAST {Settings().editorial.reporter_items} items
            - Only suggest content from companies sites and blogs if they discuss release of new products or services. 
              Posts about existing services and best practices are not welcome.
            - The readers of the magazine are professionals, AVOID articles about broad reviews of topics and trends, focus and actual novelties, breakthroughs and updates
            - Make sure the URL ID you provide direct to the exact article you chose (and not to a some news aggregation). Search for the specific URL ID of the article if needed
            - Your response should be formatted as JSON, where the items titles (meaning: the titles of the 
              articles you read) are the keys, and the values are the items IDs.
            Example:
            ```json
            {{"OpenAI's Sora text-to-video generator will be publicly available later this year": 367}}
            ```
            REMEMBER: You are competing with the rest of the staff on finding the most interesting items, so be
            creative in your searches, don't just copy paste the editor's instructions!
            """.strip())
        guidelines = '\n'.join(s.lstrip() for s in guidelines.split('\n'))
        reporters_task = editor_response.content + '\n' + guidelines
        self.logger.debug(reporters_task)

        arxiv_task = dedent(
            f"""
            You are the given the task of conducting academic-papers research for the magazine.
            Search for the latest developments in the fields of {Settings().editorial.subject}, find relevant papers
            in these fields and return a list of up to {Settings().editorial.reporter_items} such papers, which you believe are the
            most novel and groundbreaking from those you read. You are given the freedom of returning no papers at all if you believe there's
            nothing exciting to share with the magazine's professional readers.
            Return your response as a JSON, where the keys are the papers names and the values are their IDs:
            ```json
            {{"Realizing limit cycles in dissipative bosonic systems": 24}}
            ```
            Return an empty JSON if there are no results: `{{}}`
            """.strip())
        
        tasks: list[str] = [reporters_task] * len(self.reporters)
        tasks[0] = arxiv_task

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(reporter.do, task, as_json=True) for reporter, task in zip(self.reporters, tasks)]
        results = [f.result() for f in futures]
        self.logger.debug([r.content for r in results])

        suggestions: list[list[ItemSuggestion]] = []
        for i, reporter_suggestions_dict in enumerate([r.json for r in results]):
            reporter_suggestions: list[ItemSuggestion] = []
            for title, url_id in reporter_suggestions_dict.items():
                url = self.viewed_urls[url_id]
                reporter_suggestions.append(ItemSuggestion(id=url_id, title=title, url=url, reporter=self.reporters[i].name or ''))
            suggestions.append(reporter_suggestions)
        return suggestions
    
    def _select_items(self, suggestions: list[list[ItemSuggestion]]) -> list[list[ItemSuggestion]]:
        """
        1) provides a list of items from a list of suggestions, and 2) ranks those
        items by returning a JSON response indicating the selected items with their
        respective rankings and lists of similar items. Additionally, it removes
        duplicate or overly similar items from the list if necessary.

        Args:
            suggestions (list[list[ItemSuggestion]]): list of suggested items
                provided by staff, which must be ranked and evaluated based on
                their novelty, relevance, and quality.

        Returns:
            list[list[ItemSuggestion]]: a list of selected items, ranked and
            categorized according to the provided guidelines.

        """
        suggestions_text = '\n'.join([f'* {s.title} (From: {domain_of_url(s.url)}) | item ID: {s.id}' for s in flatten(suggestions)])
        task = dedent(
            f"""
            The list below contains the items suggestions provided by your staff:
            {suggestions_text}
            Your task is to select the top ~{Settings().editorial.final_items} (but no less than {Settings().editorial.final_items - 2}) from this list to be featured in today's issue.
            Note that as your reporters worked independently, some suggestions might be duplicates (either
            same topic from different sources or even the exact same item). Make sure to select {Settings().editorial.final_items} DIFFERENT
            items of different topics. Also, there should be no more than {Settings().editorial.max_academic_papers} items from arxiv.
            Rank your selection from 1 to {Settings().editorial.final_items}, where 1 is the top item of today's issue.
            Return your selection as JSON, where the item ID is the key, and the value is another dictionary, holding
            your chosen rank and a list of similar item IDs to that item, if any. 
            See the example below:
            ```json
            {{
                "ITEM_ID": 
                {{
                    "rank": int_value,
                    "similar": ["ID_OF_SIMILAR_ITEMS", ...]  // keep empty if none
                }}
            }}
            ```
            Guidelines:
            - Never rank two items which are considered similar! Choose your favorite, list the rest under the `similar` list.
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

        second_task = dedent(
            """
            Verify the items you chose - or too similar ones - did not already appear on previous issues of the magazine, as this might cause the readers to frown upon your 
            magazine, believing it is unprofessional.
            You can query the magazine archive in order to find older articles.
            For every item in the list you ranked, you now have the following options:
            - If you found it is a duplicate or overly similar to a previous article in the magazine, you can choose to remove it from today's issue
            - If you found similar entries in previous issues, but still believe it should be featured in today's issue (perhaps because of a development on the issue or for any other reason you choose), keep it and link it to the older articles
            - If you found no similar articles or entries in the archive, leave the item as it is
            Return your decision in the following JSON format:
            ```json
            {
                "ITEM_ID":
                {
                    "remove": boolean,  // whether to remove this item or not
                    "archive": ["TITLE_OF_LINKED_ITEM_FROM_ARCHIVE", ...]  // keep empty if none 
                }
            }
            ```
            Tip: Don't query just the title, try more than one query to be sure!
            """.strip())
        result = self.editor.do(second_task, as_json=True, conversation=result.conversation)
        if 'error' in result.json.keys():
            result = self.editor.do(second_task, as_json=True)
        self.logger.debug(result.content)
        remaining = result.json 

        for str_suggestion_id, dct in ranking.items():
            if remaining.get(str_suggestion_id, {}).get('remove', False):
                continue
            s_id = int(str_suggestion_id)
            indices = list(range(len(suggestions)))
            shuffle(indices)
            for i in indices:
                reporter_suggestions = suggestions[i]
                reporter_s_ids = [sg.id for sg in reporter_suggestions]
                if s_id in reporter_s_ids:
                    idx = reporter_s_ids.index(s_id)
                    suggestion = reporter_suggestions[idx]
                    suggestion.rank = int(dct['rank'])
                    suggestion.similar_ids = [int(x) for x in dct.get('similar', [])]
                    suggestion.previous_titles = remaining.get(str_suggestion_id, {}).get('archive', [])
                    reporter_suggestions[idx] = suggestion
                    break
        return suggestions
    
    def _write_items(self, items: list[list[ItemSuggestion]]) -> list[list[ItemSuggestion]]:
        """
        Takes a list of items and reporters, executes editor tasks on each item
        using the corresponding reporter, and returns the edited items with their
        text content.

        Args:
            items (list[list[ItemSuggestion]]): list of `ItemSuggestion` objects
                that will be processed by the `reporter_tasks` function, which
                contains the URL IDs and other information for each item to be summarized.

        Returns:
            list[list[ItemSuggestion]]: a list of `ItemSuggestion` objects, each
            with a summary and an `error` field indicating whether the item was
            removed or not.

        """
        error_message = "<ERROR>"
        remove_message = "<REMOVE>"
        
        def editor_task(text: str, max_words: int) -> str:
            """
            Is designed to assist with editing a provided text according to a set
            of specified guidelines. The function takes no input parameters, returns
            an edited version of the text, and allows for either minimal or no
            editing depending on user preferences.

            Args:
                text (str): final article written by one of your reporters that
                    needs to be reviewed and edited based on your magazine's guidelines.
                max_words (int): maximum number of words allowed for the edited
                    article, and the function will only accept responses that are
                    within this limit.

            Returns:
                str: a revised version of the provided text, if editing was deemed
                necessary, or the original text if no changes were made.

            """
            task = dedent(
                f"""
                The text below is the final article written by one of your reporters.
                Review it, and edit it if you fell it is necessary in order for it to meet your magazine's guidelines.
                Still, try to intervene as les as possible, if at all. Do so only if you find it to be necessary.
                Also, you have the option not to use this article in you magazine, if you believe it does not mee your standards
                or will have no value to your professional readers. 
                - If you choose to remove this article, reply only with {remove_message}
                - If you wish to keep it, reply only with the final version of your edited version. It must not exceed {max_words}!
                  Also, your response will be used as it is, so do not add any other remarks but the text. 
                - If you choose not to edit the text at all, copy the text as it is, word for word
                """)
            result = self.editor.do(f"{task}\n---\n{text}")
            return result.content
        
        def reporter_tasks(reporter: Assistant, reporter_items: list[ItemSuggestion]) -> list[ItemSuggestion]:  
            """
            Takes an list of items, checks if each item's rank is less than 0, and
            then performs the following tasks for each item: summary generation,
            editorial task completion, error handling, and ranking modification.

            Args:
                reporter (Assistant): object that performs the task of generating
                    summaries for the given items, by executing the provided `do()`
                    method to get the summaries.
                reporter_items (list[ItemSuggestion]): list of items, which are
                    summarized and edited based on predefined guidelines.

            Returns:
                list[ItemSuggestion]: a list of `reporter_item` objects, each with
                a summarized text and an error flag.

            """
            for i, item in enumerate(reporter_items):
                if item.rank < 0:
                    continue

                is_paper: bool = 'arxiv' in domain_of_url(item.url)

                if is_paper:
                    max_words = Settings().editorial.max_words_per_academic_paper
                else:
                    max_words = Settings().editorial.max_words_per_item

                task = dedent(
                    f"""
                    Read URL ID {item.id} and summarize it.
                    Follow these guidelines:
                    - It should be no more than {max_words} words{'. Break down non-intuitive or non-trivial terms to make sure all readers understand the paper and its core message' if is_paper else ''}
                    - Do NOT add a title, the editor will add it later
                    - Your response is printed as it is, so do not add any other remarks beside the summary
                    - Use Markdown syntax

                    IMPORTANT: If you encounter an error or an issue completing this task, simple respond with "{error_message}".
                    """)
                result = reporter.do(task)
                if not error_message in result.content:
                    text = result.content
                    edited_text = editor_task(text, max_words)
                    if remove_message in edited_text:
                        item.rank = -1
                    else:
                        item.text = edited_text
                else:
                    item.rank = -1
                    item.error = True
                reporter_items[i] = item
            return reporter_items
        
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(reporter_tasks, reporter, reporter_items) for reporter, reporter_items in zip(self.reporters, items)]
        items_with_text = [f.result() for f in futures]
        self.logger.debug('\n\n'.join(s.text for s in flatten(items_with_text) if s.text))
        return items_with_text

    def _get_elapsed_time(self) -> str:
        """
        Calculates and returns a timedelta object representing the elapsed time
        between `start_time` and the current moment, based on the number of minutes
        and seconds passed.

        Returns:
            str: a time delta representation in the format `minutes:seconds`.

        """
        elapsed_time = time() - self.start_time
        delta = timedelta(minutes=elapsed_time//60, seconds=elapsed_time%60)
        return str(delta)
    
    def _create_title_and_subtitle(self, full_article: str) -> dict[str, str]:
        """
        Generates a title and subtitle for an article based on provided input,
        returning them in JSON format.

        Args:
            full_article (str): text of the article that needs to be given a title
                and subtitle, which is provided as the input for the function.

        Returns:
            dict[str, str]: a JSON object containing the generated title and
            subtitle in the format `{ "title": "YOUR TITLE", "subtitle": "YOUR
            SUBTITLE" }`.

        """
        task = dedent(
            f"""
            The text below is the full article to be published today in your magazine:
            ---
            {full_article}
            ---
            Write a title and subtitle for it. Title should be up to 10 words, and subtitle up to 20 words.
            Remember your magazine is a DAILY magazine, so make sure the title isn't about the whole month or year.
            Also, make it sound professional, not amateur. Try making the title down-to-earth. It supposes to let the reader know what is in the article, not just be eay-catching.
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
    
    def _write_markdown_article(self, items: list[ItemSuggestion], twitter_urls: list[int]) -> str:
        """
        Takes an item, an list of previous articles, and an list of similar items
        as input, then creates a Markdown article with the provided item and
        previous/similar items information.

        Args:
            items (list[ItemSuggestion]): list of articles to be summarized and
                ranked based on their relevance and popularity.
            twitter_urls (list[int]): list of URLs of tweets related to the articles,
                which are then converted into Markdown format using the
                `_tweets_markdown` function.

        Returns:
            str: a Markdown-formatted article containing a summarized version of
            the input article, along with related articles and social media cards.

        """
        remove_pipes = lambda s: s.replace(" | ", " ").replace("|", " ")
        pdf_icon = lambda domain: "<img src=\"{{ 'images/pdf.png' | relative_url }}\" style='vertical-align: middle; width: 1.2em;' /> " if 'arxiv' in domain else ''

        items = sorted(items, key=lambda s: s.rank if s.rank > 0 else 999)
        md_ranked_articles = []
        md_inaccessible_articles = []
        md_unranked_articles = []
        ranked_ids = [item.id for item in items if item.rank > 0]
        ids_of_written = []
        
        for item in items:
            item_domain = domain_of_url(item.url)

            if item.id in ids_of_written:
                continue

            elif item.error:
                md_inaccessible_articles.append(f"* [{pdf_icon(item_domain)}{remove_pipes(item.title)}]({item.url}) ({item_domain})")
            
            elif item.rank == -1: 
                if item.id not in ranked_ids:
                    u = item.url.split("://")[-1]
                    if u.endswith("/"): 
                        u = u[:-1]
                    if u != item_domain:
                        md_unranked_articles.append(f'* [{pdf_icon(item_domain)}{remove_pipes(item.title)}]({item.url})')
            else:
                similar_items = []
                for s_id in item.similar_ids:
                    sim_list = [im for im in items if im.id == s_id]
                    if len(sim_list) == 0:
                        continue
                    sim = sim_list[0]
                    sim_item_domain = domain_of_url(sim.url)
                    if sim_item_domain == item_domain:
                        continue
                    similar_items.append(f'> * [{pdf_icon(sim_item_domain)}{remove_pipes(sim.title)}]({sim.url}) ({sim_item_domain})')
                    ids_of_written.append(sim.id)
                if similar_items:
                    similar_items = ["\n> **See also:**"] + similar_items
                similar_text = '\n'.join(similar_items)

                previous_titles_series: list[pd.Series] = []
                for title in item.previous_titles:
                    series = self.archive.get_by_title(title)
                    if not series.empty:
                        previous_titles_series.append(series)
                previous_titles_texts: list[str] = []
                if previous_titles_series:
                    prev_df = pd.DataFrame(previous_titles_series)
                    prev_df['dt'] = pd.to_datetime(prev_df['date'])
                    prev_df = prev_df.sort_values('dt', ascending=False)
                    remove_margin = "style='margin-bottom: 0;'"
                    for _, series in prev_df.iterrows():
                        previous_titles_texts.append(f"{{% assign article_title = \"{series['title']}\" | slugify %}}\n * [{remove_pipes(series['title'])}](" + "{{ '" + series['page'].replace('-', '/', 3) + f"#' | append: article_title" + " | relative_url }}" + f") {series['date']}")
                    previous_titles_texts = ([f"\n<blockquote class='previous-titles' markdown='1' {remove_margin if similar_items else ''}>\n**Previous headlines:**\n"] + previous_titles_texts + ["</blockquote>"])
                previous_titles_text = '\n'.join(previous_titles_texts)
                
                md_ranked_articles.append(f"# {item.title}\n_Summarized by: {item.reporter}_ [[{pdf_icon(item_domain)}{item_domain}]({item.url})]{previous_titles_text}{similar_text}\n\n{item.text}")
            ids_of_written.append(item.id)


        self.logger.info(f"Creating title for article [elapsed time: {self._get_elapsed_time()}, cost: {self.cost()}$]", color='green')
        
        self.logger.info(f"Creating title for article [elapsed time: {self._get_elapsed_time()}, cost: {self.cost()}$]", color='green')
        full_article = '\n\n'.join(md_ranked_articles)
        if md_inaccessible_articles:
            full_article += ('\n\n<h3><strong>💡 More articles for you:</strong></h3>\n\n' + '\n'.join(md_inaccessible_articles))
        if twitter_urls:
            full_article += ('\n\n' + self._tweets_markdown(twitter_urls))
        full_article += ('\n\n**Other headlines:**\n' + '\n'.join(md_unranked_articles))
        return full_article

    @property
    def output_dir(self) -> str:
        """
        Creates a new directory if one does not already exist at the specified
        path and returns its resolved path.

        Returns:
            str: the path of a directory where results will be stored.

        """
        top_dir = pathlib.Path(__file__).parent.parent.resolve()
        output_dir = os.path.join(top_dir, "results")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        return output_dir
    
    def _markdown_metadata(self, items: list[ItemSuggestion], title: str, subtitle: str, audio_filename: str, audio_filepath: str, audio_duration: str) -> str:
        """
        Sorts items based on their rank, then extracts titles from the resulting
        list and joins them with ' * ' followed by a blank line. It then generates
        Markdown metadata using the item titles, audio details, and various other
        metadata such as date, duration, file size, model, cost, and processing
        time. Finally, it returns a joined list of all the Markdown metadata elements.

        Args:
            items (list[ItemSuggestion]): list of dictionaries containing information
                to be added as metadata for the post, and it is sorted based on
                the value of the `rank` key in each dictionary to determine the
                order of the headers in the generated markdown output.
            title (str): title of the blog post.
            subtitle (str): 2nd line of the metadata JSON output, which displays
                the subtitle or title of the audio content.
            audio_filename (str): name of the audio file to be processed and used
                as the basis for calculating various metrics related to the audio
                duration, size, and model cost.
            audio_filepath (str): file path of the audio file to be processed and
                is used to calculate its size.
            audio_duration (str): duration of the audio file in seconds, which is
                added to the current time to calculate the total processing time.

        Returns:
            str: a series of key-value pairs representing various metadata elements
            for an article or other text content, including title, subtitle, audio
            filename, date, duration, and more.

        """
        headers_items = sorted([item for item in items if item.rank > 0], key=lambda s: s.rank)
        headers = [item.title for item in headers_items]
        headers_text = ' * ' + '<br /> * '.join(headers)
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
            headers: "{headers_text}"
            ---
            """.strip())
        return '\n'.join(s.lstrip() for s in metadata.split('\n'))
    
    def _create_embeddings_file(self, items: list[ItemSuggestion], filename: str, item_type: str) -> None:
        """
        Takes a list of items with rank information as input, sorts them based on
        their rank, generates embeddings for each item using an `Embedder`, and
        creates a CSV file containing the relevant information for each item.

        Args:
            items (list[ItemSuggestion]): list of dictionaries that contain text
                and rank values to be embedded into the visualization.
            filename (str): file path where the results will be saved as a CSV file.
            item_type (str): type of items to be generated embeddings for, and it
                is used to specify the appropriate embedding dimensions for each
                type of item in the list of ranked items.

        """
        rows: list[dict] = []
        date = datetime.now().strftime("%Y-%m-%d")
        ranked_items = sorted([item for item in items if item.rank > 0], key=lambda s: s.rank)
        embeddings = Embedder().generate_embeddings([item.text for item in ranked_items])
        for i, item in enumerate(ranked_items):
            rows.append({
                'date': date,
                'page': filename,
                'title': item.title,
                'url': item.url,
                'text': item.text,
                'type': item_type,
                'embedding': embeddings[i]
            })
        pd.DataFrame(rows).to_csv(os.path.join(self.output_dir, f'{filename}.csv'), header=True, index=False)

    def _tweets_markdown(self, tweets_urls: list[int]) -> str:
        """
        Takes a list of tweet URLs as input and generates an HTML code to display
        them on a web page, with a loading animation for each URL being processed.

        Args:
            tweets_urls (list[int]): list of tweet URLs that are to be embedded
                with the code, and it is used to generate the corresponding HTML
                content for each tweet.

        Returns:
            str: a concatenation of HTML code snippets for each provided tweet URL.

        """
        def embedded_tweet_html(url: str) -> str:
            """
            Generates a HTML string for a Twitter embedded tweet based on given
            URL and formatting options.

            Args:
                url (str): URL to be loaded and displayed within a `div` element
                    with a loading indicator.

            Returns:
                str: a string of HTML code containing a loading message and a URL
                link to the original tweet.

            """
            html = dedent(
                f"""
                <blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
                <div class="loading" style="width: 100%; border-left: 0px;"><a href="{url}">Loading: {url.split('//', 1)[-1]}</a></div>
                </blockquote>
                """.strip())
            return '\n'.join(s.lstrip() for s in html.split('\n'))
        
        if tweets_urls:
            htmls = [embedded_tweet_html(self.viewed_urls[url_id]) for url_id in tweets_urls]
            htmls = ["## Trending on Twitter"] + htmls + ['<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>']
            return '\n'.join(htmls)
        else:
            return ''

    def _get_stats_string(self) -> str:
        return f"[elapsed time: {self._get_elapsed_time()}, cost: {self.cost()}$]"

    def do(self) -> None:
        """
        Generates high-quality documentation for given code by: (1) starting a
        time clock; (2) logging various events using the `logger` object; (3)
        hiring an editor, reporters, and a Twitter analyst; (4) performing trend
        analysis and research; (5) selecting top items; (6) writing articles; (7)
        composing an article's markdown content; (8) creating embeddings; and (9)
        narrating the article into an MP3 file.

        """
        self.start_time = time()

        self.logger.info("Starting - Hiring editor", color='green')
        self.editor =  self._hire_editor()
        
        self.logger.info(f"Hiring staff {self._get_stats_string()}", color='green')
        self.reporters, self.twitter_analyst = self._hire_reporters()
        
        self.logger.info(f"Performing Twitter trends analysis {self._get_stats_string()}", color='green')
        twitter_trends, twitter_urls = self._twitter_analysis()

        self.logger.info(f"Performing research {self._get_stats_string()}", color='green')
        suggestions = self._research(twitter_trends) 

        self.logger.info(f"Selecting top items {self._get_stats_string()}", color='green')
        suggestions = self._select_items(suggestions) 

        self.logger.info(f"Writing articles {self._get_stats_string()}", color='green')
        items = flatten(self._write_items(suggestions))
        
        self.logger.info(f"Composing article {self._get_stats_string()}", color='green')
        full_article = self._write_markdown_article(items, twitter_urls)
        title_and_subtitle = self._create_title_and_subtitle(full_article)
        title_and_subtitle['title'] = title_and_subtitle['title'] or f'AI News: {datetime.now().strftime("%A, %d %B, %Y")}'
        title_and_subtitle['subtitle'] = title_and_subtitle['subtitle'] or "All the latest news about AI, brought to you by AI"

        alphanumeric_title = re.sub(r'[^A-Za-z0-9 ]+', '', title_and_subtitle["title"])
        filename = f'{datetime.now().strftime("%Y-%m-%d")}-{alphanumeric_title.lower().replace(" ","-")}'

        self.logger.info(f"Creating embeddings {self._get_stats_string()}", color='green')
        self._create_embeddings_file(items, filename, item_type='daily_ai_summary')

        self.logger.info(f"Narrating {self._get_stats_string()}", color='green')
        recording_filepath = os.path.join(self.output_dir, filename+'.mp3')
        output_audio = Narrator().narrate(items, title=title_and_subtitle['title'])
        length_seconds = int(len(output_audio) / 1000)
        output_audio.export(recording_filepath, format="mp3")

        minutes, seconds = divmod(length_seconds, 60)
        duration_str = "{:02d}:{:02d}".format(int(minutes), int(seconds))

        filepath = os.path.join(self.output_dir, filename+'.md')
        with open(filepath, 'w') as f:
            f.write(self._markdown_metadata(items=items, title=title_and_subtitle['title'], subtitle=title_and_subtitle['subtitle'], audio_filename=filename+".mp3", audio_filepath=recording_filepath, audio_duration=duration_str) + '\n\n')
            f.write(full_article + '\n\n')  
            f.write(f'---\n### Technical details\nCreated at: {datetime.now().strftime("%d %B, %Y, %H:%M:%S")}, ' + 'using `{{ page.model }}`.\n\nProcessing time: {{ page.processing }}, cost: {{ page.cost }}$\n')
            f.write(f'<details>\n<summary>The Staff</summary>\n<div markdown="1">\nEditor: {self.editor.name}\n\n```\n{self.editor.definition}\n```\n\n')
            f.write('\n\n'.join([f'{reporter.name}:\n\n```\n{reporter.definition}\n```' for reporter in self.reporters]))
            f.write("\n</div>\n</details>\n")
        
        self.logger.info(f"Done. {self._get_stats_string()}", color='green')
        
