#!/usr/bin/env python
import prompt


def hello():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')


def invite_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def result_play():
    from random import randint
    from math import sqrt
    random_number = randint(0, 501)

    print('Question: ', random_number)
    if random_number < 2:
        return 'no'
    if random_number == 2:
        return 'yes'
    limit = sqrt(random_number)
    i = 2
    while i <= limit:
        if random_number % i == 0:
            return 'no'
        i += 1
    return 'yes'


def round_game_1():
    check_play = result_play()
    answer = prompt.string('Your answer: ')
    if answer == check_play:
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
    if answer == check_play:
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
    if answer == check_play:
        print('Correct!')
        print('Congratulations, ', name, '!', sep='')
        return True
    else:
        print("'", answer, "'", " is wrong answer ;(.\
 Correct answer was ", "'", check_play, "'", sep='')
        print("Let's try again, ", name)
        return False
