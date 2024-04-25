from argparse import ArgumentParser
from .color_logger import set_default_log_level, get_logger
from .settings import Settings
from .routine import Routine
from .cost import Cost


def run():
    parser = ArgumentParser()
    parser.add_argument('--archive', dest='archive', help='Path to archive directory', required=True, type=str)
    parser.add_argument('-l', '--log-level', default='INFO', dest='log', help='Set logging level', type=str)
    args = parser.parse_args()
    
    set_default_log_level(args.log.upper())
    Settings().archive = args.archive
    Routine().do()
    get_logger().info(f"Costs breakdown: {Cost().report()}", color='magenta')
