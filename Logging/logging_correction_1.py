import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.WARNING)

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

def init_system_logging():
    logger.debug("Message from DEBUG")
    logger.info("Message from INFO")
    logger.warning("Message from WARNING")
    logger.error("Message from ERROR")
    logger.critical("Message from CRITICAL")

init_system_logging()

