
import re
import pkg_resources
from pypdf import PdfReader
from typing import TypeVar

T = TypeVar('T')

def path_to_resource(filename: str) -> str:
    return pkg_resources.resource_filename('techbyai', f'resources/{filename}')


def flatten(lst: list[list[T]]) -> list[T]:
    return [x for xs in lst for x in xs]


def ordinal_number(num: int) -> str:
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    # I'm checking for 10-20 because those are the digits that
    # don't follow the normal counting scheme. 
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        # the second parameter is a default.
        suffix = suffixes.get(num % 10, 'th')
    return str(num) + suffix


def read_pdf(file_path: str) -> str:
    def remove_page_numbers(text: str):
        # Pattern: newline, one or more digits, newline
        pattern = r'^(?:\d+\n)|(\n\d+\n)|(\n\d+$)|^\d+$'
        return re.sub(pattern, '\n', text) 
         
    pdf = PdfReader(file_path)
    texts: list[str] = list()
    for page in pdf.pages:
        text = page.extract_text(0)
        text = remove_page_numbers(text)
        texts.append(text)
    return " ".join(texts)
