import random
from random import randint


class Game(object):

    answer = 0
    guess = 0
    count = 0
    win = False
    current_score = 0
    total_score = 0

    def __init__(self, start_range, end_range):
        self.s_range = start_range
        self.e_range = end_range

    @staticmethod
    def random_generator():
        Game.answer = random.randint(int(s_range), int(e_range))
        # print('The answer is {}'.format(Game.answer))
        return Game.answer

    @staticmethod
    def score_system(s):
        Game.current_score = s
        Game.current_score += (s_range - e_range)

    @staticmethod
    def guess_game():
        if Game.guess < Game.answer:
            print("Higher")
            return
        elif Game.guess > Game.answer:
            print("Lower")
            return
        else:
            print("Congratulations! You guessed the right number after {} tries.".format(str(Game.count)))
            Game.win = True

    def game_system(self):
        while not Game.win:
            Game.guess = int(input('The number is between {}-{}. \nGuess the number: '.format(s_range, e_range)))
            Game.count += 1
            print(Game.win)
            self.guess_game()


if __name__ == '__main__':
    print('Hello and welcome to The Guessing Game! The goal of'
          '\nthe game is to guess the number that is randomly'
          '\npicked between a range provided by you.\n\n\n')

    s_range = input('Enter the starting range integer: ')
    print(s_range)
    e_range = input('Enter the ending range integer: ')
    print(e_range)

    g = Game(s_range, e_range)
    g.random_generator()
    g.game_system()
