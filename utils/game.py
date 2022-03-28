import random
from utils.constants import COUNTRIES


def start_game():
    country = random.choice(COUNTRIES)
    print(country)
