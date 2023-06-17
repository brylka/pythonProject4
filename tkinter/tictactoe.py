import tkinter as tk
from tkinter import messagebox

# root window
root = tk.Tk()
root.title('Kółko i krzyżyk')

# game state
board = ['' for _ in range(9)]  # 9 empty slots
current_player = 'X'
win = False


def click(cell):
    global current_player
    global win
    if board[cell] == '':  # if cell is empty
        board[cell] = current_player  # mark it with current player's symbol
        buttons[cell].config(text=current_player)  # update button text

        # check if game is won
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                                (0, 4, 8), (2, 4, 6)]  # diagonals

        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
                messagebox.showinfo("Koniec gry", f"Wygrał gracz {current_player}")
                win = True

        # check if game is draw
        if '' not in board and win == False:
            messagebox.showinfo("Koniec gry", "Remis")

        # switch current player
        current_player = 'O' if current_player == 'X' else 'X'


# create buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text='', command=lambda cell=i: click(cell), height=3, width=6)
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

root.mainloop()
