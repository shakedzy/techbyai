from dataclasses import dataclass, asdict, field


@dataclass
class ItemSuggestion:
    id: int
    title: str
    url: str
    reporter: str
    rank: int = -1
    similar_ids: list[int] = field(default_factory=list)
    previous_titles: list[str] = field(default_factory=list)
    text: str = ""
    error: bool = False

    as_dict = asdict 
