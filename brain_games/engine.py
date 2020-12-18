import prompt

count_rounds = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print(game.DESCRIPTION)
    count_correct_answer = 0
    while count_correct_answer < count_rounds:
        round_question, correct_answer = game.round()
        print("Question: {}".format(round_question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            count_correct_answer += 1
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(.\
 Correct answer was '{}'.".format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break
    if count_correct_answer == count_rounds:
        print("Congratulations, {}".format(name))
