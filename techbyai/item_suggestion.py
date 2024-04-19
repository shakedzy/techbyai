import re
from dataclasses import dataclass, asdict, field


@dataclass
class ItemSuggestion:
    title: str
    url: str
    reporter: str
    rank: int = -1
    similar_ids: list[str] = field(default_factory=list)
    previous_titles: list[str] = field(default_factory=list)
    text: str = ""

    @property
    def id(self) -> str:
        return self.title[0].upper() + str(int(hash(self.url)%99999))
    
    @property
    def alphanumeric_title(self) -> str:
        t = re.sub(r'[^A-Za-z0-9 ]+', '', self.title)
        return t.replace(' ', '-').lower()
    
    as_dict = asdict 
