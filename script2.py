import tkinter as tk
import random

class TicTacToeGUI:

    def __init__(self):
        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]
        self.create_gui()

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.root, text='', width=10, height=5, command=lambda index=i: self.button_click(index))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)
        self.result_label = tk.Label(self.root, text='', font=('Helvetica', 20))
        self.result_label.grid(row=3, columnspan=3)
        self.restart_button = tk.Button(self.root, text='Restart', command=self.restart_game)
        self.restart_button.grid(row=4, columnspan=3)

    def restart_game(self):
        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.config(text='')
        self.result_label.config(text='')

    def button_click(self, index):
        if self.board[index] == ' ':
            self.buttons[index].config(text=self.current_player)
            self.board[index] = self.current_player
            if self.check_win():
                self.result_label.config(text=f"{self.current_player} wins!")
            elif self.check_tie():
                self.result_label.config(text="It's a tie!")
            else:
                self.current_player = 'O'
                self.bot_play()

    def bot_play(self):
        # Pick a random empty spot for the bot
        empty_spots = [i for i in range(9) if self.board[i] == ' ']
        bot_choice = random.choice(empty_spots)
        self.buttons[bot_choice].config(text='O')
        self.board[bot_choice] = 'O'
        if self.check_win():
            self.result_label.config(text=f"O wins!")
        elif self.check_tie():
            self.result_label.config(text="It's a tie!")
        else:
            self.current_player = 'X'

    def check_win(self):
        win_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != ' ':
                return True
        return False

    def check_tie(self):
        return ' ' not in self.board

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    game = TicTacToeGUI()
    game.run()
