import bord


def person_game_loop():
    while True:
        bord.how_to_play()
        choice = input("Choose your mark (X or O): ").lower()
        if choice not in ["x", "o"]:
            print("Invalid choice. Please choose X or O.")
            continue
        else:
            first_player = choice
            second_player = "o" if first_player == "x" else "x"
        bord.init_bord()
        for turn in range(9):
            current_player = first_player if turn % 2 == 0 else second_player
            print(f"It's {current_player.upper()}'s turn")
            move = bord.choose_move(bord.bord)
            bord.make_move(bord.bord, move, current_player)

            if turn >= 4:
                if bord.game_end(bord.bord):
                    break
            else:
                continue
        print("=" * 20)
        break


def computer_game_loop():
    while True:
        bord.how_to_play()
        choice = input("Choose your mark (X or O): ").lower()
        if choice not in ["x", "o"]:
            print("Invalid choice. Please choose X or O.")
            continue
        else:
            first_player = choice
            second_player = "o" if first_player == "x" else "x"
        bord.init_bord()
        for turn in range(9):
            current_player = first_player if turn % 2 == 0 else second_player
            if current_player == first_player:
                print(f"It's {current_player.upper()}'s turn")
                move = bord.choose_move(bord.bord)
            else:
                move = bord.computer_move(bord.bord)
                print(f"Computer chose move: {move}")

            bord.make_move(bord.bord, move, current_player)

            if turn >= 4:
                if bord.game_end(bord.bord):
                    break
            else:
                continue
        print("=" * 20)
        break
