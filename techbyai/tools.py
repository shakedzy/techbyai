import re
import os
import json
import arxiv
import inspect
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from typing import Any, Callable
from .color_logger import get_logger
from .settings import Settings
from .utils import read_pdf
from .archive import Archive
from ._types import ToolsDefType


def handle_tool_error(e: Exception) -> None:
    get_logger().error(f'ERROR [{e.__class__.__name__} in {inspect.stack()[1].function}]: {str(e)}', color='red')


### TOOLS ###

def web_search(query: str) -> str:
    """
    Search the web for the provided query, and returns the title, URL and description of the results.
    Search results are separated by: =====

    Example of two search results:

    Title: Welcome to My Site
    URL: http://www.mysite.xyz
    Description: This is my private website, see my stuff here
    =====
    Title: Grapes Online
    URL: http://www.grapes.com
    Description: This is the number one site for grapes fans and lovers
    """
    MAX_RESULTS = 10
    sites_filter = ' '.join([f'-site:{domain}' for domain in Settings().search.blacklist])
    try:
        results = []
        service = build("customsearch", "v1", developerKey=os.environ['GOOGLE_SEARCH_API_KEY'])
        response = service.cse().list(
            # Google CSE API docs: https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
            q=f"{query} {sites_filter}", 
            cx=os.environ['GOOGLE_SEARCH_CSE_ID'], 
            num=MAX_RESULTS,
            dateRestrict=f'd{Settings().search.past_days}'
            ).execute()
        
        if 'items' not in response:
            get_logger().debug(f'Query: {query} yielded no results!')
            return "No results"
        
        for result in response['items']:
            results.append((result['title'], result['link'], result['snippet']))

        if results:
            return '\n=====\n'.join(f"Title: {title}\nURL: {url}\nDescription: {body}\n" for (title, url, body) in results)
        else:
            return "No results"

    except Exception as e:
        handle_tool_error(e)
        return f"Error while searching the web: {e}"


def search_for_tweets(usernames: list[str], query: str = '') -> str:
    """
    Search the web for tweets from the given list of Twitter user-names.
    Every result is provided with the page title and full URL.
    Results are separated by: =====
    """
    twitter_filter = ' OR '.join([f"site:twitter.com/{u.strip('@')}" for u in usernames])
    return web_search(f'{query} ({twitter_filter})')


def visit_website(url: str) -> str:
    """
    Goes to the provided URL and returns a simple version of the page text. Images and styling are excluded.
    """
    try:
        headers = {'User-Agent': Settings().web.user_agent}
        response = requests.get(url, timeout=Settings().web.surf_timeout_seconds, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()

            # Clean whitespaces
            text = re.sub(pattern=r'[ \t]+', repl=' ', string=text)  # Replace multiple spaces and tabs with a single space
            text = re.sub(pattern=r'\n{3,}', repl='\n\n', string=text)  # Replace more than two newlines with two newlines
            text = text.strip()

            return text 
        else:
            raise RuntimeError(f"ERROR: Failed to retrieve the webpage. Status code: {response.status_code}")
    except Exception as e:
        handle_tool_error(e)
        return f"ERROR: {e}"


def new_ai_research_from_arxiv() -> str:
    """
    Returns a list of AI related papers, their IDs on arXiv, their URLs and their summaries in the following format:

    Title: Realizing limit cycles in dissipative bosonic systems
    ID: 2401.05332v1
    URL: https://arxiv.org/pdf/2401.05332
    Summary: We propose a general mechanism for generating limit cycle (LC) oscillations
    by coupling a linear bosonic mode to a dissipative nonlinear bosonic mode...
    predictions.
    =====
    Title: Fermi polaron in atom-ion hybrid systems
    ID: 2401.05324v1
    URL: https://arxiv.org/pdf/2401.05324
    Summary: Charged quasiparticles dressed by the low excitations of an electron gas,
    constitute one of the fundamental pillars for understanding quantum many-body...
    """
    try:
        search = arxiv.Search(
            query="cs.AI",
            sort_by=arxiv.SortCriterion.SubmittedDate
        )
        results = arxiv.Client().results(search)
        now = datetime.now().date()

        results_strings = []
        for r in results:
            if r.published.date() < now - timedelta(days=Settings().search.past_days):
                break
            paper_id = r.get_short_id()
            results_strings.append(f"Title: {r.title}\nID: {paper_id}\nURL: {r.pdf_url}\nSummary: {r.summary}")
        
        get_logger().info(f"Found {len(results_strings)} new papers on arXiv")
        if results_strings:
            return "\n=====\n".join(results_strings)
        else:
            return "No results"
    
    except Exception as e:
        handle_tool_error(e)
        return f"ERROR: {e}"


def get_arxiv_paper(paper_id: str) -> str:
    """
    Returns the full text of the requested ID paper from arXiv.
    """
    try:
        arxiv_paper = next(arxiv.Client().results(arxiv.Search(id_list=[paper_id])))
        file_name = f'paper_{paper_id}.pdf'
        arxiv_paper.download_pdf(filename=file_name)
        content = read_pdf(file_name)
        return content
    except Exception as e:
        handle_tool_error(e)
        return f"ERROR: {e}"


def query_magazine_archive(query: str, archive: Archive) -> str:
    """
    Return a the title, URL, date of publish and text of the top 3 articles from the magazine's archive which
    match the query. 
    Results are returned in JSON format.
    """
    top_results = archive.query(query, 3)
    if top_results.empty:
        return "No results"
    
    output: list[dict[str, str]] = []
    for _, row in top_results.iterrows():
        output.append({
            'title': row['title'], 
            'url': row['url'],
            'date': row['date'],
            'text': row['text']
            })
    return json.dumps(output)


#######

            
TOOLS_PARAMS_DEFINITIONS: ToolsDefType = {
    web_search: [("query", {"type": "string", "description": "The query to search on the web"}, True)],
    visit_website: [("url", {"type": "string", "description": "The URL of the page to visit"}, True)],
    search_for_tweets: [("usernames", {"type": "array", "items": {"type": "string"}, "description": "A list of Twitter usernames to limit the search to"}, True),
                        ("query", {"type": "string", "description": "The query to search in tweets"}, False)],
    new_ai_research_from_arxiv: [],
    get_arxiv_paper: [("paper_id", {"type": "string", "description": "The arXiv ID of the paper to fetch"}, True)],
    query_magazine_archive: [("query", {"type": "string", "description": "The query to search in the archive magazine"}, True)]
}


WEB_TOOLS = [web_search, visit_website]
TWITTER_TOOLS = [search_for_tweets]
ARXIV_TOOLS = [new_ai_research_from_arxiv, get_arxiv_paper]
MAGAZINE_TOOLS = [query_magazine_archive]


def build_tools(functions: list[Callable]) -> list[dict[str, Any]]:
        tools = list()
        for func in functions:
            v = TOOLS_PARAMS_DEFINITIONS.get(func, [])
            params = {}
            required = []
            for p in v:
                params[p[0]] = p[1]
                if p[2]: 
                    required.append(p[0])

            tools.append({
                "type": "function",
                "function": {
                    "name": func.__name__,
                    "description": func.__doc__,
                    "parameters": {
                        "type": "object",
                        "properties": params
                    },
                    "required": required
                }
            })
        return tools
