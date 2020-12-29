from random import randint, choice

DESCRIPTION = 'What number is missing in the progression?'
lenght_of_progression = 10


def create_progression(start, step, lenght):
    finish = start + lenght * step
    progressions = [i for i in range(start, finish, step)]
    return progressions


def give_data_for_round():
    start_progression = randint(1, 99)
    step_progression = randint(3, 10) * choice([-1, 1])
    index_hidden_number = randint(0, lenght_of_progression - 1)
    progressions = create_progression(
        start_progression, step_progression, lenght_of_progression)
    check_play = progressions[index_hidden_number]
    progressions[index_hidden_number] = '..'
    correct_answer = check_play
    round_question = ' '.join([str(i) for i in progressions])
    return round_question, str(correct_answer)
