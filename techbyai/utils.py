import re
import pkg_resources
from urllib.parse import urlparse
from pypdf import PdfReader
from typing import TypeVar


T = TypeVar('T')


def path_to_resource(filename: str) -> str:
    return pkg_resources.resource_filename('techbyai', f'resources/{filename}')


def domain_of_url(url: str) -> str:
    return urlparse(url).netloc


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


def get_version() -> str:
    return pkg_resources.get_distribution("techbyai").version


def dedent(text: str) -> str:
    def count_leading_whitespaces(line: str) -> tuple[int, str]:
        stripped = line.lstrip()
        return len(line) - len(stripped), stripped
    
    leading_whitespace_count = -1
    lines = text.splitlines()
    output: list[str] = []
    for line in lines:
        whitespaces_count, stripped = count_leading_whitespaces(line)
        if stripped:  # Check if the line is non-empty (i.e., it contains non-whitespace characters)
            if leading_whitespace_count < 0:
                leading_whitespace_count = whitespaces_count
                output.append(stripped)
            else:
                if whitespaces_count <= leading_whitespace_count:
                    output.append(stripped)
                else:
                    output.append(line[leading_whitespace_count:])
        else:
            output.append("")
    return "\n".join(output)


def lowercase_keys(d: dict[str, T]) -> dict[str, T]:
    return {k.lower(): (lowercase_keys(v) if isinstance(v, dict) else v) for k, v in d.items()}
