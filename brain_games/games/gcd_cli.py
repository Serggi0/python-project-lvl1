from random import randint

condition = 'Find the greatest common divisor of given numbers.'


def calculate(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return max(number1, number2)


def round():
    random_number1 = randint(1, 51)
    random_number2 = randint(1, 51)
    elements = [str(random_number1), str(random_number2)]
    round_question = ' '.join(elements)
    correct_answer = str(calculate(random_number1, random_number2))
    return round_question, correct_answer
