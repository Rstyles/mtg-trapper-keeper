import cmd
from models import card
from repositories import mtg_repository


class MtgConsole(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = "MTG> "
        self.mtg_repo = mtg_repository.MTGRepository()

    def do_list(self, arg):
        cards = self.mtg_repo.get_cards()
        for card in cards:
            print(card)
        page = 1
        while True:
            cont = input("Would you like to continue listing cards? (y/n): ").strip().lower()
            if cont == 'y':
                page += 1
                cards = self.mtg_repo.get_cards(page)
                for card in cards:
                    print(card)
            elif cont == 'n':
                break
            else:
                print("Please enter 'yes' or 'no'.")


    def do_search(self, arg):
        card_name = arg
        card = self.mtg_repo.get_card_by_name(card_name)
        if card:
            print(card)
        else:
            print(f"Card with name '{card_name}' not found")

    def do_exit(self, arg):
        return True

if __name__ == "__main__":
    MtgConsole().cmdloop();
