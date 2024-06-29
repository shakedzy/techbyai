from pydantic import BaseModel, RootModel, field_validator


class StringStringJSONWithCustomKeys(RootModel[dict[str, str]]):
    @field_validator('root', mode='before')
    def check_keys_and_values_are_strings(cls, value, info):
        if not isinstance(value, dict):
            raise ValueError('Must be a dictionary')
        
        for key, val in value.items():
            if not isinstance(key, str):
                raise ValueError(f'Key {key} is not a string')
            if not isinstance(val, str):
                raise ValueError(f'Value {val} is not a string')
        return value


class ChosenItems(BaseModel):
    items: list[int]

    @field_validator('items', mode='before')
    def check_items_are_integers(cls, value, info):
        if not isinstance(value, list):
            raise ValueError('Must be a list of integers')
        if not all(isinstance(item, int) for item in value):
            raise ValueError('List must contain only integers')
        return value


class TweetsAndTrends(BaseModel):
    topics: list[str]
    tweets: list[int]

    @field_validator('topics', mode='before')
    def check_topics_are_strings(cls, value, info):
        if not isinstance(value, list):
            raise ValueError('Must be a list of strings')
        
        for topic in value:
            if not isinstance(topic, str):
                raise ValueError(f'Topic {topic} is not a string')
        return value
    
    @field_validator('tweets', mode='before')
    def check_tweets_are_ints(cls, value, info):
        if not isinstance(value, list):
            raise ValueError('Must be a list of integers')
        
        for tweet in value:
            if not isinstance(tweet, int):
                raise ValueError(f'Tweet {tweet} is not an integer')
        return value
    

class SingleSelectedItem(BaseModel):
    rank: int
    similar: list[str]

    @field_validator('rank', mode='before')
    def check_rank_is_int(cls, value, info):
        if not isinstance(value, int):
            raise ValueError('Must be an integer')
        return value
    
    @field_validator('similar', mode='before')
    def check_similar_are_strings(cls, value, info):
        if not isinstance(value, list):
            raise ValueError('Must be a list of strings')
        
        for topic in value:
            if not isinstance(topic, str):
                raise ValueError(f'Topic {topic} is not a string')
        return value


class SelectedItems(RootModel[dict[str, SingleSelectedItem]]):
    @field_validator('root', mode='before')
    def check_root_is_dict(cls, value, info):
        if not isinstance(value, dict):
            raise ValueError('Must be a dictionary')
        
        for key in value:
            if not isinstance(key, str):
                raise ValueError(f'Key {key} is not a string')
            if not key.isnumeric():
                raise ValueError(f'Key {key} is not a numeric string')
        return value
    

class SingleRemovableItem(BaseModel):
    remove: bool
    archive: list[str]

    @field_validator('remove', mode='before')
    def check_remove_is_bool(cls, value, info):
        if not isinstance(value, bool):
            raise ValueError('Must be a boolean')
        return value
    
    @field_validator('archive', mode='before')
    def check_archive_are_strings(cls, value, info):
        if not isinstance(value, list):
            raise ValueError('Must be a list of strings')
        
        for topic in value:
            if not isinstance(topic, str):
                raise ValueError(f'Topic {topic} is not a string')
        return value
    

class RemovableItems(RootModel[dict[str, SingleRemovableItem]]):
    @field_validator('root', mode='before')
    def check_root_is_dict(cls, value, info):
        if not isinstance(value, dict):
            raise ValueError('Must be a dictionary')
        
        for key in value:
            if not isinstance(key, str):
                raise ValueError(f'Key {key} is not a string')
            if not key.isnumeric():
                raise ValueError(f'Key {key} is not a numeric string')
        return value


class TitleAndSubtitle(BaseModel):
    title: str
    subtitle: str

    @field_validator('title', mode='before')
    def check_title_is_string(cls, value, info):
        if not isinstance(value, str):
            raise ValueError('Must be a string')
        
        return value
    
    @field_validator('subtitle', mode='before')
    def check_subtitle_is_string(cls, value, info):
        if not isinstance(value, str):
            raise ValueError('Must be a string')
        
        return value
    