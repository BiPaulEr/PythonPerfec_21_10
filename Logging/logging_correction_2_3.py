import logging
import random

class MyFilter(logging.Filter):
    def filter(self, record):
        if "AJOUTE" in record.msg:
            return False
        return True

livres_logger = logging.getLogger('livres_logger')
transactions_logger = logging.getLogger('transactions_logger')

livres_logger.setLevel(logging.WARNING)
transactions_logger.setLevel(logging.WARNING)

stream_handler_livres = logging.StreamHandler()
form_livres = logging.Formatter("%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s", datefmt="%d/%m/%Y %H:%M")
stream_handler_livres.setFormatter(form_livres)
filter = MyFilter()
stream_handler_livres.addFilter(filter)

stream_handler_transactions = logging.StreamHandler()
form_transactions = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_handler_transactions.setFormatter(form_transactions)

livres_logger.addHandler(stream_handler_livres)
transactions_logger.addHandler(stream_handler_transactions)

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
