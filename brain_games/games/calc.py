from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def calculate(number1, operator, number2):
    if operator == '+':
        expression = number1 + number2
    elif operator == '-':
        expression = number1 - number2
    elif operator == '*':
        expression = number1 * number2
    return expression


def play_round():
    operators = ['+', '-', '*']
    random_number1 = randint(1, 101)
    random_number2 = randint(1, 10)
    random_operator = choice(operators)
    round_question = "{} {} {}".format(
        random_number1, random_operator, random_number2)
    correct_answer = str(
        calculate(random_number1, random_operator, random_number2))
    return round_question, correct_answer
