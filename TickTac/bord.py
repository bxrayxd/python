import random


bord = [" " for _ in range(9)]


def display_bord(bord):
    print("\n")
    print(f"  {bord[0]} | {bord[1]} | {bord[2]} ")
    print(" ---+---+---")
    print(f"  {bord[3]} | {bord[4]} | {bord[5]} ")
    print(" ---+---+---")
    print(f"  {bord[6]} | {bord[7]} | {bord[8]} ")
    print("\n")


def init_bord():
    bord = [" " for _ in range(9)]
    display_bord(bord)


def make_move(bord, move, player):
    bord[move - 1] = player.upper()
    display_bord(bord)


def how_to_play():
    print("Welcome to Tic Tac Toe!")
    print("The board positions are numbered as follows:")
    print(" 1 | 2 | 3 ")
    print(" ---+---+---")
    print(" 4 | 5 | 6 ")
    print(" ---+---+---")
    print(" 6 | 8 | 9 ")
    print("\n")
    print("Players take turns to place their mark (X or O) in an empty cell.")
    print("The first player to get three marks in a row wins.")
    print("Good luck!\n")


def game_end(bord):
    if check_winner(bord):
        return True
    else:
        return False


def check_winner(bord):
    for i in range(3):
        if bord[i * 3] == bord[i * 3 + 1] == bord[i * 3 + 2] != " ":
            print(f"Player {bord[i * 3].capitalize()} wins!")
            return True

    for i in range(3):
        if bord[i] == bord[i + 3] == bord[i + 6] != " ":
            print(f"Player {bord[i].capitalize()} wins!")
            return True

    if bord[0] == bord[4] == bord[8] != " ":
        print(f"Player {bord[0].capitalize()} wins!")
        return True

    if bord[2] == bord[4] == bord[6] != " ":
        print(f"Player {bord[2].capitalize()} wins!")
        return True
    if " " not in bord:
        print("It's a draw!")
        return True
    return False


def available_moves(bord) -> list:
    available_move = []
    for i in range(9):
        if bord[i] == " ":
            available_move.append(i + 1)
    return available_move


def choose_move(bord) -> int:
    while True:
        print("avaliabe moves are", available_moves(bord))
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 0 < int(move) <= 9:
            move = int(move)
            if bord[move - 1] == " ":
                return move
            else:
                print("This cell is already occupied. Try again.")
                continue
        else:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue


def computer_move(board) -> int:
    move = available_moves(board)
    return random.choice(move) if move else -1
