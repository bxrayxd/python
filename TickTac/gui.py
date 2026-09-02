import tkinter as tk
from tkinter import messagebox


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = "O"
        self.board = [" " for _ in range(9)]

        self.buttons = []
        self.status_label = tk.Label(
            root, text="Player O's turn", font=("Arial", 14))
        self.status_label.pack()

        self.frame = tk.Frame(root)
        self.frame.pack()

        for i in range(9):
            button = tk.Button(
                self.frame,
                text=" ",
                font=("Arial", 20),
                width=5,
                height=2,
                command=lambda i=i: self.make_move(i),
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.reset_button = tk.Button(
            root, text="Restart", command=self.reset_board)
        self.reset_button.pack(pady=10)

    def make_move(self, index):
        if self.board[index] != " ":
            return

        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player, state="disabled")

        if self.check_winner():
            self.status_label.config(
                text=f"Player {self.current_player} wins!")
            messagebox.showinfo("Game Over", f"Player {
                                self.current_player} wins!")
            self.disable_all_buttons()
        elif " " not in self.board:
            self.status_label.config(text="It's a draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            self.current_player = "X" if self.current_player == "O" else "O"
            self.status_label.config(
                text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        b = self.board
        wins = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for x, y, z in wins:
            if b[x] == b[y] == b[z] != " ":
                return True
        return False

    def disable_all_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_board(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "O"
        self.status_label.config(text="Player O's turn")
        for btn in self.buttons:
            btn.config(text=" ", state="normal")
