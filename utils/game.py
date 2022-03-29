import random
from utils.constants import COUNTRIES
from utils.user import get_user_choice


def get_solution(country, user_choices):
    output = ""
    for ch in country:
        if ch in user_choices:
            output += ch
        else:
            output += "_"
    return output


def start_game():
    country = random.choice(COUNTRIES)
    print(country)
    chrs = set(country)
    user_choices = []
    lifes = 3
    while lifes > 0:
        output = get_solution(country, user_choices)
        print(output)
        user_input = get_user_choice(user_choices)
        user_choices.append(user_input)
        if user_input in country:
            correct_choices = chrs.intersection(user_choices)
            if len(chrs) == len(correct_choices):
                break
            continue
        lifes -= 1
