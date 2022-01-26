from random import choice


class Fortune:
    def game(self, user):
        self.result = 0
        monsters = ["Centaur", "Minotaur", "Hydra"]
        c = choice(monsters)
        question = choice(monsters)
        answer = input(f"Who behind the door {question}? ")
        if user > 0:
            if answer == "I believe" and c == question or answer == "I do not believe" and c != question:
                print(f"Behind the door {c}")
                self.result = user * 2
                print(f"Hooray! You win!: ${self.result}")
            if answer == "I believe" and c != question or answer == "I do not believe" and c == question:
                print(f"Behind the door {c}")
                self.result = 0
                print(f"Hooray! You win!: ${self.result}")
        elif user < 0:
            if answer == "I believe" and c == question or answer == "I do not believe" and c != question:
                print(f"Behind the door {c}")
                self.result = 0
                print(f"Oops, you lose!: ${self.result}")
            if answer == "I believe" and c != question or answer == "I do not believe" and c == question:
                print(f"Behind the door {c}")
                self.result = user * 2
                print(f"Alas, but you lose!: ${self.result}")
