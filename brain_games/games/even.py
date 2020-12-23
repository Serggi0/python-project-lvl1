from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True


def play_round():
    round_question = randint(0, 101)
    if is_even(round_question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return round_question, correct_answer
