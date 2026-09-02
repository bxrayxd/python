import game

while True:
    print("\nEnter C for playing with computer")
    print("Enter P for playing with another player")
    print("Enter Q to quit")

    mood = input("Your choice: ").lower()

    if mood == "q":
        print("Goodbye!")
        break
    elif mood == "p":
        game.person_game_loop()
    elif mood == "c":
        game.computer_game_loop()
    else:
        print("Invalid input. Please enter C, P, or Q.")
