from random import randint

condition = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculate(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def round():
    random_number = randint(0, 101)
    correct_answer = calculate(random_number)
    return random_number, correct_answer
