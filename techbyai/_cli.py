from argparse import ArgumentParser
from .color_logger import set_default_log_level
from .settings import init_settings, Settings
from .routine import Routine
from .utils import path_to_resource


def run():
    parser = ArgumentParser()
    parser.add_argument('--embdir', dest='embdir', help='Path to embeddings file directory', required=True, type=str)
    parser.add_argument('-l', '--log-level', default='INFO', dest='log', help='Set logging level', type=str)
    args = parser.parse_args()
    
    set_default_log_level(args.log.upper())
    init_settings([path_to_resource("config.toml")])
    Settings().embeddings.directory = args.embdir
    Routine().do()
