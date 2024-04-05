import pkg_resources
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
