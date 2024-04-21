from techbyai.settings import init_settings
from techbyai.utils import path_to_resource
from techbyai.tools import get_raw_tweet


init_settings([path_to_resource('config.toml')])
print(get_raw_tweet("https://twitter.com/MichaelRapaport/status/1762963414005985516"))
