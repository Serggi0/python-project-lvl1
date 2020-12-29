from random import randint
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def give_data_for_round():
    number1 = randint(1, 51)
    number2 = randint(1, 51)
    round_question = "{} {}".format(number1, number2)
    correct_answer = str(math.gcd(number1, number2))
    return round_question, correct_answer
