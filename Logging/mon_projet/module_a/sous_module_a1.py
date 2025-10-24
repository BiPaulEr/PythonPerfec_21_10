import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler= logging.FileHandler("test.log")
logger.addHandler(file_handler)

def fonction_a1():
    logger.debug("Exécution de fonction_a1 dans sous_module_a1.")
