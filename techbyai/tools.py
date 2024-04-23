import re
import os
import json
import arxiv
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
from ._decorators import tool


### TOOLS ###

@tool
def web_search(query: str) -> str:
    """
    Search the web for the provided query, and returns the title, URL and description of the results.
    Results are returned as JSON.

    [{
        "title": "Welcome to My Site",
        "url": "http://www.mysite.xyz",
        "description": "This is my private website, see my stuff here"
    }]
    """
    MAX_RESULTS = 10
    sites_filter = ' '.join([f'-site:{domain}' for domain in Settings().search.blacklist])
    results: list[dict[str, str]] = []
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
        return "{'empty': 'No results'}"
    
    for result in response['items']:
        results.append({"title": result['title'], "url": result['link'], "description": result['snippet']})

    if results:
        return json.dumps(results)
    else:
        return "{'empty': 'No results'}"


@tool
def search_for_tweets(usernames: list[str], query: str = '') -> str:
    """
    Search the web for tweets from the given list of Twitter user-names.
    Every result is provided with the page title and full URL.
    Results are returned as JSON.
    """
    twitter_filter = ' OR '.join([f"site:twitter.com/{u.strip('@')}" for u in usernames])
    return web_search(f'{query} ({twitter_filter})')


@tool
def visit_website(url: str) -> str:
    """
    Goes to the provided URL and returns a simple version of the page text. Images and styling are excluded.
    """
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
        raise RuntimeError(f"Failed to retrieve the webpage. Status code: {response.status_code}")


@tool
def validate_url(url: str) -> str:
    """
    Verifies the URL is live and returns no errors.
    Returns "OK" if everything is fine or "ERROR" if the URL is unreachable.
    """
    headers = {'User-Agent': Settings().web.user_agent}
    response = requests.get(url, timeout=Settings().web.surf_timeout_seconds, headers=headers)
    if response.status_code == 200:
        return "OK"
    else:
        return "ERROR"


@tool
def new_ai_research_from_arxiv() -> str:
    """
    Returns a list of AI related papers, their IDs on arXiv, their URLs and their summaries as JSON in the following format:

    [{
        "title": "Realizing limit cycles in dissipative bosonic systems",
        "id": "2401.05332v1",
        "url": "https://arxiv.org/pdf/2401.05332"
        "summary": "We propose a general mechanism for generating limit cycle (LC) oscillations..."
    }]
    """
    search = arxiv.Search(
        query="cs.AI",
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    arxiv_results = arxiv.Client().results(search)
    now = datetime.now().date()

    results = []
    for r in arxiv_results:
        if r.published.date() < now - timedelta(days=Settings().search.past_days):
            break
        paper_id = r.get_short_id()
        results.append({f"title": r.title, "id": paper_id, "url": r.pdf_url, "summary": r.summary})
    
    get_logger().info(f"Found {len(results)} new papers on arXiv")
    if results:
        return json.dumps(results)
    else:
        return "{'empty': 'No results'}"


@tool
def get_arxiv_paper(paper_id: str) -> str:
    """
    Returns the full text of the requested ID paper from arXiv.
    The paper ID is found in its URL, usually as the last part of it.
    For example, if the URL of a paper is "https://arxiv.org/pdf/2401.05332.pdf" 
    or "https://arxiv.org/pdf/2401.05332", then the ID is "2401.05332"
    """
    arxiv_paper = next(arxiv.Client().results(arxiv.Search(id_list=[paper_id])))
    file_name = f'paper_{paper_id}.pdf'
    arxiv_paper.download_pdf(filename=file_name)
    content = read_pdf(file_name)
    return content


@tool
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


WEB_TOOLS = [web_search, visit_website, validate_url]
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
