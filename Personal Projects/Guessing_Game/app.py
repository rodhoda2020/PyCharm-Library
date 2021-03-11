from random import randint


class Game(object):

    def __init__(self, s_range, e_range):
        self.s_range = s_range
        self.e_range = e_range

    @staticmethod
    def random_generator():
        answer = randint(int(s_range), int(e_range))
        # print('The answer is {}'.format(answer))
        return answer

    @staticmethod
    def score_system(s):
        score = s
        score += (s_range - e_range)
        return score

    def guess_game(self):
        return


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
