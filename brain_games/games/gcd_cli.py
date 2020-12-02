#!/usr/bin/env python
import prompt


def hello():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')


def invite_game():
    print('Find the greatest common divisor of given numbers.')


def result_play():
    from random import randint
    random_number1 = randint(0, 101)
    random_number2 = randint(0, 101)
    print('Question: ', random_number1, random_number2)
    while random_number1 != 0 and random_number2 != 0:
        if random_number1 > random_number2:
            random_number1 = random_number1 % random_number2
        else:
            random_number2 = random_number2 % random_number1
    return max(random_number1, random_number2)


def round_game_1():
    check_play = result_play()
    answer = prompt.string('Your answer: ')
    if answer == str(check_play):
        print('Correct!')
        return True
    else:
        print("'", answer, "'", " is wrong answer ;(.\
 Correct answer was ", "'", check_play, "'", sep='')
        print("Let's try again, ", name)
        return False


def round_game_2():
    check_play = result_play()
    answer = prompt.string('Your answer: ')
    if answer == str(check_play):
        print('Correct!')
        return True
    else:
        print("'", answer, "'", " is wrong answer ;(.\
 Correct answer was ", "'", check_play, "'", sep='')
        print("Let's try again, ", name)
        return False


def round_game_3():
    check_play = result_play()
    answer = prompt.string('Your answer: ')
    if answer == str(check_play):
        print('Correct!')
        print('Congratulations, ', name, '!', sep='')
        return True
    else:
        print("'", answer, "'", " is wrong answer ;(.\
 Correct answer was ", "'", check_play, "'", sep='')
        print("Let's try again, ", name)
        return False
