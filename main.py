import random
from utils.constants import COUNTRIES

if __name__ == "__main__":
    country = random.choice(COUNTRIES)

    while True:
        print("1. Start Game!")
        print("2. End Game!")
        customer = input("Please write your option: ")
        if customer == "1":
            pass
        elif customer == "2":
            break


