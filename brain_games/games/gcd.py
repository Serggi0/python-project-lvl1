from random import randint
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def is_gcd(number1, number2):
    return math.gcd(number1, number2)


def round():
    random_number1 = randint(1, 51)
    random_number2 = randint(1, 51)
    elements = [str(random_number1), str(random_number2)]
    round_question = ' '.join(elements)
    correct_answer = str(is_gcd(
        random_number1, random_number2))
    return round_question, correct_answer
