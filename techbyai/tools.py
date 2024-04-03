import re
import os
import inspect
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from .color_logger import get_logger
from .settings import Settings
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
    try:
        results = []
        service = build("customsearch", "v1", developerKey=os.environ['GOOGLE_SEARCH_API_KEY'])
        response = service.cse().list(
            # Google CSE API docs: https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
            q=query, 
            cx=os.environ['GOOGLE_SEARCH_CSE_ID'], 
            num=MAX_RESULTS,
            dateRestrict=f'd{Settings().search.past_days}'
            ).execute()
        for result in response['items']:
            results.append((result['title'], result['link'], result['snippet']))

        if results:
            return '\n=====\n'.join(f"Title: {title}\nURL: {url}\nDescription: {body}\n" for (title, url, body) in results)
        else:
            return "No results"

    except Exception as e:
        handle_tool_error(e)
        return f"Error while searching the web: {e}"


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


#######

            
tools_params_definitions: ToolsDefType = {
    web_search: [("query", {"type": "string", "description": "The query to search on the web"}, True)],
    visit_website: [("url", {"type": "string", "description": "The URL of the page to scrape"}, True)],
}
