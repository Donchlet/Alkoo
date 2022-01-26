import random
from Module.Compare import CompareCards


class BlackJack:
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.player = [random.choice(self.cards), random.choice(self.cards)]
        self.computer = [random.choice(self.cards), random.choice(self.cards)]
        self.die_or_win = [0, 0, 1000, 0]

    def game(self):
        print('Choose option: ')
        print('1. Draw cards')
        print('2. Draw cards only to player')
        print('3. Draw cards only to computer')
        print('4. Russian Roulette')
        print(f'Your cards: {sum(self.player)}')
        print(f'Computer cards: {sum(self.computer)}')
        choice = int(input('Your choice: '))
        while True:
            compare_1 = CompareCards(player_list=self.player,
                                     computer_list=self.computer)
            if choice == 1:
                self.player.append(random.choice(self.cards))
                self.computer.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break

            elif choice == 2:
                self.player.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break

            elif choice == 3:
                self.computer.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
            elif choice == 4:
                self.player.append(random.choice(self.die_or_win))
                self.computer.append(random.choice(self.die_or_win))
                if compare_1.compare_results():
                    break


        restart = input('\nDo you want to restart the game: ')
        if restart == 'y':
            black = BlackJack()
            black.game()
        else:
            pass


black_cards = BlackJack()
black_cards.game()












