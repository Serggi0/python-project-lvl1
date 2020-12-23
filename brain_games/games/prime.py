from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_if_prime(number):
    if number < 2:
        return 'no'
    elif number == 2:
        return 'yes'
    else:
        for i in range(2, number):
            if number % i == 0:
                return 'no'
        return 'yes'


def play_round():
    round_question = randint(0, 101)
    correct_answer = check_if_prime(round_question)
    return round_question, correct_answer
