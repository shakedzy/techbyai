from pkg_resources import get_distribution
from .color_logger import set_default_log_level
from .settings import init_settings
from .routine import Routine
from .utils import path_to_resource


def _get_version_from_setuptools():
    return get_distribution("techbyai").version


def main():
    set_default_log_level("INFO")
    init_settings([path_to_resource("config.toml")])
    Routine().do()


__version__ = _get_version_from_setuptools()
