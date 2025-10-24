import logging
from logging.handlers import RotatingFileHandler
import time
# Configuration du logger
logger = logging.getLogger('RotatingLog')
logger.setLevel(logging.DEBUG)

# Configuration du RotatingFileHandler
handler = RotatingFileHandler('rotating_log_example.log', maxBytes=1024*100, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Génération de logs pour tester la rotation des fichiers
for i in range(10000):
    time.sleep(0.005)
    logger.debug(f"Ceci est le message de log numero {i}")

print("Logging avec RotatingFileHandler terminé. Vérifiez les fichiers de log.")
