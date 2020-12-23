from random import randint
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(number1, number2):
    return math.gcd(number1, number2)


def play_round():
    random_number1 = randint(1, 51)
    random_number2 = randint(1, 51)
    round_question = "{} {}".format(random_number1, random_number2)
    correct_answer = str(find_gcd(random_number1, random_number2))
    return round_question, correct_answer
