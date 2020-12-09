import prompt

count_rounds = 3


def hello(cli):
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')
    print(cli.condition)


def run_game(cli):
    count_correct_answer = 0
    hello(cli)
    while count_correct_answer < count_rounds:
        round_question, correct_answer = cli.round()
        print('Question: ', round_question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            count_correct_answer += 1
            print('Correct!')
        else:
            print("'", user_answer, "'", " is wrong answer ;(.\
 Correct answer was ", "'", correct_answer, "'", ".", sep='')
            print("Let's try again, ", name, "!", sep='')
            break
    if count_correct_answer == count_rounds:
        print('Congratulations, ', name, '!', sep='')
