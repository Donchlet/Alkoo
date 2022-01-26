import random


class PythonCasino:
    def __init__(self, player):
        self.combination_red = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.combination_black = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.lucky_red = random.choice(self.combination_red)
        self.lucky_black = random.choice(self.combination_black)
        self.player = player

    def compare_combination(self, choice_red, choice_black):
        if choice_red == self












