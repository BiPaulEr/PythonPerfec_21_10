import logging
from logging.handlers import TimedRotatingFileHandler
import time

# Configuration du logger
logger = logging.getLogger('TimedRotatingLog')
logger.setLevel(logging.DEBUG)

# Configuration du TimedRotatingFileHandler
# Rotation définie toutes les minutes ('M'), avec 3 fichiers de sauvegarde
handler = TimedRotatingFileHandler('time_rotating_log_example.log', when='M', interval=1, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Génération de logs pour tester la rotation des fichiers basée sur le temps
for _ in range(60):
    logger.debug("Ceci est un message de test pour TimeRotatingFileHandler.")
    time.sleep(10)

print("Logging avec TimeRotatingFileHandler terminé. Vérifiez les fichiers de log.")
