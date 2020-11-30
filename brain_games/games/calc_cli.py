#!/usr/bin/env python
import prompt
from random import randint, choice


list_operator = ['+', '-', '*']
count_rounds = 3


def hello():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')


def calc_game():
    i = 0
    print('What is the result of the expression?')
    while i < count_rounds:
        random_number1 = randint(1, 101)
        random_number2 = randint(1, 10)
        random_operator = choice(list_operator)
        if random_operator == '+':
            expression = random_number1 + random_number2
        elif random_operator == '-':
            expression = random_number1 - random_number2
        elif random_operator == '*':
            expression = random_number1 * random_number2
        print('Question: ', random_number1, random_operator, random_number2)
        answer = prompt.string('Your answer: ')
        if answer == str(expression):
            print('Correct!')
            i += 1
        else:
            print("'", answer, "'", " is wrong answer ;(.\
 Correct answer was ", "'", expression, "'", sep='')
            print("Let's try again, ", name)
            break
    if i == count_rounds:
        print('Congratulations, ', name, '!', sep='')
