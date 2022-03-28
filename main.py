from utils.game import start_game
if __name__ == "__main__":

    while True:
        print("1. Start Game!")
        print("2. End Game!")
        customer = input("Please write your option: ")
        if customer == "1":
            start_game()
        elif customer == "2":
            break


