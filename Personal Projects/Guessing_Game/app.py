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
        answer = random.randint(int(s_range), int(e_range))
        print('The answer is {}'.format(Game.answer))
        return Game.answer

    @staticmethod
    def score_system(s):
        Game.current_score = s
        Game.current_score += (s_range - e_range)


    @staticmethod
    def guess_game():
        if Game.guess == Game.answer:
            print("Hurray, you guessed the correct number!")
        elif Game.guess > Game.answer:
            print("It's less than that.")
        else:
            print("It's more than that.")

    def game_system(self):
        Game.guess = int(input('The number is between {}-{}. \nGuess the number: '.format(s_range, e_range)))
        # print(guess)
        while Game.win == False:
            if Game.guess == Game.answer:
                print("Congratulations! You guessed the right number after {} tries.".format(Game.count))
                Game.Win = True
            else:
                self.guess_game()
                Game.count += 1





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
    g.guess_game()
