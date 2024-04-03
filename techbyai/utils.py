import pkg_resources
from typing import TypeVar

T = TypeVar('T')

def path_to_resource(filename: str) -> str:
    return pkg_resources.resource_filename('techbyai', f'resources/{filename}')


def flatten(lst: list[list[T]]) -> list[T]:
    return [x for xs in lst for x in xs]
