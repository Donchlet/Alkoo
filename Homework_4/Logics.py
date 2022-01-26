from random import choice


class Asino:
    def __init__(self, balance, chance):
        if isinstance(balance, int):
            self.balance = balance
            self.chance = chance

    def game(self, numbers, wager):
        list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                           23, 24, 25, 26, 27, 28, 29, 30]
        random_choice = choice(list_of_numbers)
        print(f"You chose: {numbers}\n"
              f"You gave: {wager}")
        if random_choice == numbers:
            self.chance += wager
            print(f"Result: {random_choice}")
            print(f"Hooray! You win! ${wager}!")
            return True
        elif random_choice != numbers:
            self.balance -= wager
            self.chance -= wager
            print(f"Result: {random_choice}")
            print(f"Oops, you lose: ${wager}")
            return True
        else:
            print("Something is gone wrong...")
            return True

