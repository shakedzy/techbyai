from .color_logger import set_default_log_level
from .settings import init_settings
from .routine import Routine
from .utils import path_to_resource


def main():
    set_default_log_level("DEBUG")
    init_settings([path_to_resource("config.toml")])
    Routine().do()
