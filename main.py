from os import system
import battle

while True:
    print("----- Welcome to the Text-Based Battle Simulator -----\n")

    print("1. Start New Game")
    print("2. Load Game")
    print("3. Quit\n")

    choice = input(">> ")

    if choice == "1":
        battle.start()
    elif choice == "2":
        print("Load Game!")
        break
    elif choice == "3":
        print("Are you going to run away?")
        exit()
    system("cls")