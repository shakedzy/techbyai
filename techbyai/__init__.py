from .settings import init_settings
from .utils import path_to_resource

init_settings([path_to_resource("config.toml")])
