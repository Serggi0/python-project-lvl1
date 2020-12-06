import prompt


def hello():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')


def invite_game():
    print('What is the result of the expression?')


def result_play():
    from random import randint, choice
    list_operator = ['+', '-', '*']
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
    return expression


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
