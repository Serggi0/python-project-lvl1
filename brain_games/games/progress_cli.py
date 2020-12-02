#!/usr/bin/env python
import prompt


def hello():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')


def invite_game():
    print('What number is missing in the progression?')


def result_play():
    from random import randint, choice
    count_member_prgr = 10
    list_step_prgr = [i for i in range(-10, 11, 1)]
    list_step_prgr.remove(0)
    step_prgr = choice(list_step_prgr)
    start_prgr = randint(1, 99)
    finish_prgr = start_prgr + count_member_prgr * step_prgr
    list_prgr = [i for i in range(start_prgr, finish_prgr, step_prgr)]
    random_index = randint(1, 9)
    check_play = list_prgr[random_index]
    list_prgr[random_index] = '..'
    print('Question:', ' '.join([str(i) for i in list_prgr]))
    return check_play


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
