from random import randint
from math import sqrt

condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculate(number):
    if number < 2:
        return 'no'
    if number == 2:
        return 'yes'
    limit = sqrt(number)
    i = 2
    while i <= limit:
        if number % i == 0:
            return 'no'
        i += 1
    return 'yes'


def round():
    round_question = randint(0, 101)
    correct_answer = calculate(round_question)
    return round_question, correct_answer
