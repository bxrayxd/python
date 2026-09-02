import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.board = {i: " " for i in range(1, 10)}
        self.buttons = {}

        self.mode_var = tk.StringVar(value="computer")
        self.symbol_var = tk.StringVar(value="X")
        self.first_turn_var = tk.StringVar(value="user")

        self.create_widgets()

    def create_widgets(self):
        # Game settings
        tk.Label(self.root, text="Play With").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(
            self.root, text="Computer", variable=self.mode_var, value="computer"
        ).grid(row=0, column=1)
        tk.Radiobutton(
            self.root, text="Player 2", variable=self.mode_var, value="player"
        ).grid(row=0, column=2)

        tk.Label(self.root, text="Select").grid(row=1, column=0, sticky="w")
        tk.Radiobutton(self.root, text="X", variable=self.symbol_var, value="X").grid(
            row=1, column=1
        )
        tk.Radiobutton(self.root, text="O", variable=self.symbol_var, value="O").grid(
            row=1, column=2
        )

        tk.Label(self.root, text="Who starts?").grid(
            row=2, column=0, sticky="w")
        tk.Radiobutton(
            self.root, text="You", variable=self.first_turn_var, value="user"
        ).grid(row=2, column=1)
        tk.Radiobutton(
            self.root, text="Other", variable=self.first_turn_var, value="computer"
        ).grid(row=2, column=2)

        tk.Button(self.root, text="Start/restart", command=self.start_game).grid(
            row=3, column=1, pady=5
        )

        # Board buttons
        for i in range(3):
            for j in range(3):
                idx = i * 3 + j + 1
                btn = tk.Button(
                    self.root,
                    text=" ",
                    width=6,
                    height=3,
                    command=lambda i=idx: self.user_move(i),
                )
                btn.grid(row=4 + i, column=j)
                self.buttons[idx] = btn

    def start_game(self):
        self.board = {i: " " for i in range(1, 10)}
        for btn in self.buttons.values():
            btn.config(text=" ", state=tk.NORMAL)

        self.user_symbol = self.symbol_var.get()
        self.computer_symbol = "O" if self.user_symbol == "X" else "X"
        self.current_turn = self.first_turn_var.get()
        self.vs_computer = self.mode_var.get() == "computer"

        if self.vs_computer and self.current_turn == "computer":
            self.root.after(300, self.computer_move)

    def user_move(self, pos):
        if self.board[pos] == " ":
            current_symbol = (
                self.user_symbol
                if self.current_turn == "user"
                else self.computer_symbol
            )
            self.make_move(pos, current_symbol)

            if self.check_game_end():
                return

            if self.vs_computer:
                self.current_turn = "computer"
                self.root.after(300, self.computer_move)
            else:
                self.current_turn = (
                    "user" if self.current_turn == "computer" else "computer"
                )

    def make_move(self, pos, symbol):
        self.board[pos] = symbol
        self.buttons[pos].config(text=symbol, state=tk.DISABLED)

    def computer_move(self):
        move = self.find_best_move()
        if move:
            self.make_move(move, self.computer_symbol)
            if self.check_game_end():
                return
            self.current_turn = "user"

    def available_moves(self):
        return [i for i, v in self.board.items() if v == " "]

    def is_winner(self, board, symbol):
        combos = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        ]
        return any(all(board[i] == symbol for i in line) for line in combos)

    def is_draw(self):
        return all(self.board[i] != " " for i in self.board)

    def find_best_move(self):
        # Win
        for move in self.available_moves():
            copy = self.board.copy()
            copy[move] = self.computer_symbol
            if self.is_winner(copy, self.computer_symbol):
                return move

        # Block user
        for move in self.available_moves():
            copy = self.board.copy()
            copy[move] = self.user_symbol
            if self.is_winner(copy, self.user_symbol):
                return move

        # Center
        if self.board[5] == " ":
            return 5

        # Corners
        for move in [1, 3, 7, 9]:
            if self.board[move] == " ":
                return move

        # Sides
        for move in [2, 4, 6, 8]:
            if self.board[move] == " ":
                return move

        return None

    def check_game_end(self):
        for symbol in ["X", "O"]:
            if self.is_winner(self.board, symbol):
                messagebox.showinfo("Game Over", f"Player {symbol} wins!")
                self.disable_all()
                return True

        if self.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.disable_all()
            return True

        return False

    def disable_all(self):
        for btn in self.buttons.values():
            btn.config(state=tk.DISABLED)


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
