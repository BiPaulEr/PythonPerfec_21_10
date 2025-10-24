import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

file_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), "log.log"))
logger.addHandler(file_handler)

def test():
    logger.debug("DEBUG msg")
    logger.info("INFO msg")
    logger.warning("WARNING msg")
    logger.error("ERROR msg")
    logger.critical("CRITICAL msg")

test()

