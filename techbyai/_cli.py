from argparse import ArgumentParser
from .color_logger import set_default_log_level, get_logger
from .settings import Settings
from .routine import Routine


def run():
    parser = ArgumentParser()
    parser.add_argument('--archive', dest='archive', help='Path to archive directory', required=True, type=str)
    parser.add_argument('-l', '--log-level', default='INFO', dest='log', help='Set logging level', type=str)
    args = parser.parse_args()
    
    set_default_log_level(args.log.upper())
    Settings().archive = args.archive
    logger = get_logger()
    routine = Routine()
    try:
        routine.do()
    finally:
        logger.info(f"Viewed URLs:\n{routine.viewed_urls.get_all()}")
        logger.info(f"Costs breakdown (total: {routine.cost()}$): {routine.cost.report()}", color='magenta')
