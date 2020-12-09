from random import randint

condition = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculate(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def round():
    round_question = randint(0, 101)
    correct_answer = calculate(round_question)
    return round_question, correct_answer
