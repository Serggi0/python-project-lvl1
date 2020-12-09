from random import randint, choice

condition = 'What is the result of the expression?'


def calculate(number1, operator, number2):
    if operator == '+':
        expression = number1 + number2
    elif operator == '-':
        expression = number1 - number2
    elif operator == '*':
        expression = number1 * number2
    return expression


def round():
    list_operator = ['+', '-', '*']
    random_number1 = randint(1, 101)
    random_number2 = randint(1, 10)
    random_operator = choice(list_operator)
    elements = [str(random_number1), random_operator, str(random_number2)]
    round_question = ' '.join(elements)
    correct_answer = str(
        calculate(random_number1, random_operator, random_number2))
    return round_question, correct_answer
