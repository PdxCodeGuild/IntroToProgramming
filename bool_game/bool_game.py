"""
PDX Code Guild Curriculum. Boolean Game.
"""

import random

bools = {
        'not False': not False,
        'not True': not True,
        'True or False': True or False,
        'True or True': True or True,
        'False or True': False or True,
        'False or False': False or False,
        'True and False': True and False,
        'True and True': True and True,
        'False and True': False and True,
        'False and False': False and False,
        'not (True or False)': not (True or False),
        'not (True or True)': not (True or True),
        'not (False or True)': not (False or True),
        'not (False or False)': not (False or False),
        'not (True and False)': not (True and False),
        'not (True and True)': not (True and True),
        'not (False and True)': not (False and True),
        'not (False and False)': not (False and False),
        '1 != 0': 1 != 0,
        '1 != 1': 1 != 1,
        '0 != 1': 0 != 1,
        '0 != 0': 0 != 0,
        '1 == 0': 1 == 0,
        '1 == 1': 1 == 1,
        '0 == 1': 0 == 1,
        '0 == 0': 0 == 0,
        }


def random_question():
    question = random.choice(list(bools.keys()))
    answer = bools[question]

    return question, answer


def game():
    score = 0
    print('Welcome to the boolean value game!')
    print('Type (T)rue or (F)alse for each question.')

    while len(bools) > 0:
        left = len(bools)
        print("You have answered {score} of 26 questions correctly.".format(score=str(score)))
        print("There are {left} questions left.".format(left=str(left)))
        question = random_question()
        player_answer = input("What is the value of {q}?: ".format(q=question[0]))

        if player_answer.lower() == "t":
            player_answer = 'True'
        elif player_answer.lower() == 'f':
            player_answer = 'False'

        if player_answer == str(question[1]):
            print("********** That is correct! **********")
            del bools[question[0]]
            score += 1
        else:
            print("Sorry, that is not correct.")

game()
