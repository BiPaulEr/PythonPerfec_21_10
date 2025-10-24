import logging, os, yaml
import logging.config
import random

with open(os.path.join(os.path.dirname(__file__), 'logging_config.yaml'), 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    
livres_logger = logging.getLogger('livres_logger')
transactions_logger = logging.getLogger('transactions_logger')

bibliotheque = {}

def add_book(title):
    if random.random() < 0.9:
        bibliotheque[title] = True
        livres_logger.info(f"AJOUTE {title}")
    else:
        livres_logger.warning(f"PAS AJOUTE {title}")

def process_transaction(user_id, book_id):
    if bibliotheque.get(book_id):
        transactions_logger.info(f"ACHETE {user_id} {book_id}")
        del bibliotheque[book_id]
    else:
        transactions_logger.warning(f"ECHEC ACHAT {user_id} {book_id}")

livres_a_ajouter = ["Livre"+str(i) for i in range(1, 21)]
utilisateurs = ["Paul", "Dupont", "Georges"]

for livre in livres_a_ajouter:
    add_book(livre)

for index, livre in enumerate(livres_a_ajouter):
    user = utilisateurs[index % len(utilisateurs)]
    process_transaction(user, livre)
