from random import randint, choice

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(start, step, index, count_member):
    finish = start + count_member * step
    list_progression = [i for i in range(start, finish, step)]
    check_play = list_progression[index]
    list_progression[index] = '..'
    elements = ' '.join([str(i) for i in list_progression])
    return check_play, elements


def round():
    # count_member_prgr = 10
    start_prgr = randint(1, 99)
    list_step_prgr = [i for i in range(-10, 11, 1)]
    list_step_prgr.remove(0)
    step_prgr = choice(list_step_prgr)
    random_index = randint(1, 9)

    correct_answer, round_question = generate_progression(
        start_prgr, step_prgr, random_index, 10)
    return round_question, str(correct_answer)
