import random


def play():

    moves = ["R", "P", "S"]

    while True:

        user = input(
            "'R' for Rock, 'P' for Paper, 'S' for Scissors; Pick your move: \n").upper()

        if user not in moves:
            user = input(
                "Invalid Input! 'R' for Rock, 'P' for Paper, 'S' for Scissors; Pick your move: \n").upper()

        computer = random.choice(moves)

        print(f"Player({user}) : CPU({computer})")

        print("")

        if (user == "R" and computer == "S") or (user == "S" and computer == "P") or (user == "P" and computer == "R"):
            print("Player win! \n\nGame over!")
            break

        elif(computer == "R" and user == "S") or (computer == "S" and user == "P") or (computer == "P" and user == "R"):
            print("Computer win \n\nGame over!")
            break

        else:
            print("It's a Tie! \n\nPlay again!")
            continue


def main():
    print("Welcome to Rock Paper Scissors!\n\n")

    play()


if __name__ == "__main__":
    main()
