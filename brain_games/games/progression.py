from random import randint, choice

DESCRIPTION = 'What number is missing in the progression?'


def hide_number(start, step, index, count_member):
    finish = start + count_member * step
    progressions = [i for i in range(start, finish, step)]
    check_play = progressions[index]
    progressions[index] = '..'
    elements = ' '.join([str(i) for i in progressions])
    return check_play, elements


def play_round():
    number_of_progression = 10
    index_hidden_number = randint(1, 9)
    start_progression = randint(1, 99)
    progression_steps = [i for i in range(-10, 11, 1)]
    progression_steps.remove(0)
    step_progression = choice(progression_steps)
    correct_answer, round_question = hide_number(
        start_progression, step_progression,
        index_hidden_number, number_of_progression)
    return round_question, str(correct_answer)
