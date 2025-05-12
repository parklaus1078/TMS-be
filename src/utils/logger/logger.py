import logging
import sys

from src.utils.logger.logger_constants import CUSTOM_LOG_LEVEL, DB_LOG_LEVEL

logger = logging.getLogger(__name__)
formatter = logging.Formatter(fmt='%(asctime)s loglevel=%(levelname)-6s %(funcName)s() L%(lineno)-4d %(message)s')
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.handlers = [stream_handler]
logger.setLevel(getattr(logging, CUSTOM_LOG_LEVEL.upper(), logging.INFO))

pymongo_logger = logging.getLogger('pymongo')
pymongo_logger.setLevel(getattr(logging, DB_LOG_LEVEL.upper(), logging.INFO))
pymongo_logger.addHandler(stream_handler)
