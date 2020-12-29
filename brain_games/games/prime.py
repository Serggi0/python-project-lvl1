from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_if_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


def give_data_for_round():
    round_question = randint(0, 101)
    if check_if_prime(round_question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return round_question, correct_answer
