import re
import os
import json
import pytz
import arxiv
import requests
import dateutil.parser as parser
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from typing import Any, Callable
from .color_logger import get_logger
from .settings import Settings
from .utils import read_pdf, domain_of_url
from .archive import Archive
from .viewed_urls import ViewedURLs
from .cost import Cost
from .exceptions import WebSearchNoResultsException
from .package_types import ToolsDefType
from .decorators import tool


def _validate_published_date(google_search_result: dict[str, Any]) -> bool | None:
    published_date: str | None = google_search_result.get('pagemap', {}).get('metatags', [{}])[0].get('article:published_time', None)
    if not published_date: 
        return None
    dt = parser.parse(published_date, fuzzy=True).astimezone(pytz.utc)
    date_cutoff = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=Settings().search.past_days)
    date_cutoff = pytz.utc.localize(date_cutoff)
    return dt >= date_cutoff


def _is_published_today_from_text(text: str) -> bool:
    date_patterns = [
        r'\b(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})\b',                  # 12/06/2023, 12-06-2023, etc.
        r'\b(\d{1,2})(st|nd|rd|th)?\s+([A-Za-z]+)\s+(\d{2,4})\b',    # 12th June 2023, 12 June 2023
        r'\b([A-Za-z]+)\s+(\d{1,2})(st|nd|rd|th)?,?\s+(\d{2,4})\b',  # June 12, 2023, June 12th, 2023
        r'\b(\d{4})[/-](\d{2})[/-](\d{2})\b'                         # 2023-06-12, 2023/06/12
    ]
    found_dates: set[datetime] = set()
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            try:
                if len(match) == 3:
                    date_str = f"{match[0]}-{match[1]}-{match[2]}"
                    date = datetime.strptime(date_str, '%Y-%m-%d')
                elif len(match) == 4:
                    if match[0].isdigit():
                        date_str = f"{match[3]}-{match[2]}-{match[1]}"
                        date = datetime.strptime(date_str, '%Y-%m-%d')
                    else:
                        date_str = f"{match[3]} {match[0]} {match[1]}"
                        date = datetime.strptime(date_str, '%Y %B %d')
                else:
                    date_str = f"{match[2]} {match[0]} {match[1]}"
                    date = datetime.strptime(date_str, '%d %B %Y')
                found_dates.add(date)
            except ValueError:
                continue
    if len(found_dates) != 1:
        return False
    dt = found_dates.pop()
    return dt.date() >= datetime.now().date() - timedelta(days=1)


def _validate_url(url: str, *, retrieve_title: bool = False) -> bool | str:
    try:
        domain = domain_of_url(url)
        trailing = url.split(domain)[1]
        current_year = str(datetime.now().year)

        if not any(site in domain for site in ['x.com', 'twitter.com', 'arxiv.com']):
            # Check if current year is in URL (usually the date is part of an article's URL)
            if current_year not in trailing:
                # If not, assess if the URL seems long enough (as it usually is with actual articles)
                if len(trailing) < 35:
                    return False

        # Check access to site
        headers = {'User-Agent': Settings().web.user_agent}
        response = requests.get(url, timeout=Settings().web.surf_timeout_seconds, headers=headers)
        if response.status_code == 200:
            if retrieve_title:
                soup = BeautifulSoup(response.content, 'html.parser')
                title: str | None = soup.title.string if soup.title else None
                if title:
                    return title
                else:
                    return False
            else:
                return True
        else:
            return False
    except:
        return False

viewed_urls = ViewedURLs()
cost = Cost()


def _get_arxiv_paper(paper_id: str) -> str:
    """
    Returns the full text of the requested ID paper from arXiv.
    """
    arxiv_paper = next(arxiv.Client().results(arxiv.Search(id_list=[paper_id])))
    file_name = f'paper_{paper_id}.pdf'
    arxiv_paper.download_pdf(filename=file_name)
    content = read_pdf(file_name)
    return content


def _visit_website(url: str) -> str:
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


### TOOLS ###


@tool
def web_search(query: str, *, ignore_twitter: bool = True) -> str:
    """
    Search the web for the provided query, and returns the title, an ID and description of the results.
    Results are returned as JSON.

    [{
        "title": "Welcome to My Site",
        "id": 921,
        "domain": "site.com",
        "description": "This is my private website, see my stuff here"
    }]
    """
    MAX_RESULTS = 10
    try:
        blacklist: list[str] = Settings().search.blacklist
        if ignore_twitter:
            blacklist += ['twitter.com', 'x.com']

        sites_filter = ' '.join([f'-site:{domain}' for domain in blacklist])
        results: list[dict[str, str | int]] = []
        service = build("customsearch", "v1", developerKey=os.environ['GOOGLE_SEARCH_API_KEY'])

        response = service.cse().list(
            # Google CSE API docs: https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
            q=f"{query} {sites_filter}", 
            cx=os.environ['GOOGLE_SEARCH_CSE_ID'], 
            num=MAX_RESULTS,
            dateRestrict=f'd{Settings().search.past_days}'
        ).execute()
        cost.add('web_search')
        
        if 'items' not in response:
            get_logger().debug(f'Query: {query} yielded no results!')
            raise WebSearchNoResultsException()
        
        for result in response['items']:
            url = result['link']
            try:
                is_date_valid = _validate_published_date(result)
            except:
                is_date_valid = None
            
            if is_date_valid is None:
                try:
                    text = _visit_website(url)
                    is_date_valid = _is_published_today_from_text(text=text[:int(len(text)/8)])
                except:
                    is_date_valid = False

            if not is_date_valid:
                continue  
            
            title: str = (result['title'] or '').strip()
            incomplete_title: bool = title.endswith('…') or title.endswith('...')
            is_valid = _validate_url(url, retrieve_title=incomplete_title)
            if is_valid:
                if incomplete_title:
                    title: str = is_valid  # type: ignore
                url_id = viewed_urls.add(url, title=title)
                results.append({"title": title, "id": url_id, "domain": domain_of_url(url), "description": result['snippet']})

        if results:
            return json.dumps(results)
        else:
            raise WebSearchNoResultsException()
    
    except WebSearchNoResultsException:
        return '{}'


@tool
def search_for_tweets(usernames: list[str], query: str = '') -> str:
    """
    Search the web for tweets from the given list of Twitter user-names.
    Every result is provided with the page title and its ID.
    Results are returned as JSON.
    """
    twitter_filter = ' OR '.join([f"site:twitter.com/{u.strip('@')}" for u in usernames])
    return web_search(f'{query} ({twitter_filter})', ignore_twitter=False)


@tool
def new_ai_research_from_arxiv() -> str:
    """
    Returns a list of AI related papers, their IDs and their summaries as JSON in the following format:

    [{
        "title": "Realizing limit cycles in dissipative bosonic systems",
        "id": 801,
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
        url_id = viewed_urls.add(r.pdf_url, title=r.title)
        results.append({f"title": r.title, "id": url_id, "summary": r.summary})
    
    get_logger().info(f"Found {len(results)} new papers on arXiv")
    if results:
        return json.dumps(results)
    else:
        return '{}'


@tool
def get_url_id_content(url_id: int) -> str:
    """
    Retrieves the content of the provided URL ID, which could be either a web page or an arXiv paper.
    Returns the full plain text, formatting and images are excluded.
    """
    try:
        url = viewed_urls[url_id]
    except:
        get_logger().warn(f"Tried to fetch URL ID {url_id}, but it does not exist!", color='red')
        return f"ERROR: URL ID {url_id} does not exist!"
    domain = domain_of_url(url)
    if 'arxiv' in domain:
        paper_id = url.split('/')[-1].strip()
        return _get_arxiv_paper(paper_id)
    else:
        return f'[From: {domain}]\n' + _visit_website(url)

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
    get_url_id_content: [("url_id", {"type": "number", "description": "The ID provided of the URL to visit"}, True)],
    search_for_tweets: [("usernames", {"type": "array", "items": {"type": "string"}, "description": "A list of Twitter usernames to limit the search to"}, True),
                        ("query", {"type": "string", "description": "The query to search in tweets"}, False)],
    new_ai_research_from_arxiv: [],
    query_magazine_archive: [("query", {"type": "string", "description": "The query to search in the archive magazine"}, True)]
}


WEB_TOOLS = [web_search, get_url_id_content]
TWITTER_TOOLS = [search_for_tweets]
ARXIV_TOOLS = [new_ai_research_from_arxiv, get_url_id_content]
MAGAZINE_TOOLS = [query_magazine_archive]


def build_tools(functions: list[Callable]) -> list[dict[str, Any]]:
        tools = list()
        for func in set(functions):
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
