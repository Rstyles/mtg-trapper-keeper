import sqlite3

from models.card import Card

class MTGDB:
    def __init__(self):
        self.conn = sqlite3.connect("db/mtg.db", check_same_thread=False)
        self.cursor = self.conn.cursor()

        # create table if it doesn't exist
        query = "CREATE TABLE IF NOT EXISTS cards (id TEXT PRIMARY KEY, name TEXT, imageUrl TEXT, set_name TEXT)"
        self.cursor.execute(query)

    def get_cards(self) -> list[Card]:
        query = "SELECT * FROM cards"
        self.cursor.execute(query)
        cards = self.cursor.fetchall()
        collection = [];
        for card in cards:
            data = {
                "id": card[0],
                "name": card[1],
                "imageUrl": card[2],
                "set": card[3]
            }
            collection.append(Card(**data))
        return collection

    def get_card_by_name(self, name:str) -> Card:
        query = "SELECT * FROM cards WHERE name = ?"
        self.cursor.execute(query, (name,))
        card = self.cursor.fetchone()
        if card:
            data = {
                "id": card[0],
                "name": card[1],
                "imageUrl": card[2],
                "set": card[3]
            }
            return Card(**data)
        return None


    def add_card(self, card):
        query = "INSERT INTO cards (id, name, imageUrl, set_name) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (card.id, card.name, card.image_url, card.set))
        self.conn.commit()

    def delete_card(self, id):
        query = "DELETE FROM cards WHERE id = ?"
        self.cursor.execute(query, (id,))
        self.conn.commit()
