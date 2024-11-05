from models.card import Card
from db.mtg_db import MTGDB

class CollectionRepository:
    def __init__(self):
        self.db = MTGDB()

    def get_cards(self) -> list[Card]:
        return self.db.get_cards()

    def add_card(self, card):
        self.db.add_card(card)

    def delete_card(self, id):
        self.db.delete_card(id)
