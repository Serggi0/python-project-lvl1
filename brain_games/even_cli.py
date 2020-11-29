#!/usr/bin/env python
import prompt
from random import randint


def check_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        random_number = randint(0, 101)
        print('Question: ', random_number)
        answer = prompt.string('Your answer: ')
        if i <= 2:
            if random_number % 2 == 0:
                if answer == 'yes':
                    print('Correct!')
                    i += 1
                elif answer == 'no':
                    i == 0
                    print("'no' is wrong answer ;(.\
 Correct answer was 'yes'.")
                    print("Let's try again, ", name)
                    break
                else:
                    i == 0
                    print("'", answer, "'", " is wrong answer ;(.\
 Correct answer was 'yes'.", sep='')
                    break
            else:
                if answer == 'no':
                    print('Correct!')
                    i += 1
                elif answer == 'yes':
                    i == 0
                    print("'yes' is wrong answer ;(.\
 Correct answer was 'no'.")
                    print("Let's try again, ", name)
                    break
                else:
                    i == 0
                    print("'", answer, "'", " is wrong answer ;(.\
 Correct answer was 'yes'.", sep='')
                    break
        if i == 2:
            print('Congratulations, ', name, '!', sep='')
