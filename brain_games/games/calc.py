from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'
operators = ['+', '-', '*']


def calculate(num1, symbol, num2):
    if symbol == '+':
        expression = num1 + num2
    elif symbol == '-':
        expression = num1 - num2
    elif symbol == '*':
        expression = num1 * num2
    return expression


def give_data_for_round():
    number1 = randint(1, 101)
    number2 = randint(1, 10)
    operator = choice(operators)
    round_question = "{} {} {}".format(
        number1, operator, number2)
    correct_answer = str(calculate(number1, operator, number2))
    return round_question, correct_answer
