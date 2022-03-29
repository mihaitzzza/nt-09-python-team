import random

from utils.constants import COUNTRIES
from utils.user import get_user_choice


def start_game():
    country = random.choice(COUNTRIES)
    print(country)
    user_choices = []
    is_over = False
    while not is_over:
        output = ""
        for ch in country:
            if ch in user_choices:
                output += ch
            else:
                output += "_"
        print(output)

        user_input = get_user_choice(user_choices)
        user_choices.append(user_input)




