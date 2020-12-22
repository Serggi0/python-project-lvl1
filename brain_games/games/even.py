from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def round():
    round_question = randint(0, 101)
    correct_answer = is_even(round_question)
    return round_question, correct_answer
