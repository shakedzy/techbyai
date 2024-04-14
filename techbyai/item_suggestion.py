from dataclasses import dataclass, asdict, field


@dataclass
class ItemSuggestion:
    title: str
    url: str
    reporter: str
    rank: int = -1
    similar_ids: list[str] = field(default_factory=list)
    text: str = ""
    editorial_note: str = ""

    @property
    def id(self) -> str:
        return self.title[0].upper() + str(int(hash(self.url)%99999))
    
    as_dict = asdict 
