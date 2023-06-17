import tkinter as tk
from tkinter import messagebox
import random

# root window
root = tk.Tk()
root.title('Memory')

# game state
cards = [str(i//2) for i in range(16)]
random.shuffle(cards)
buttons = [tk.Button(root, text='?', width=10, height=2)
           for i in range(16)]
for i in range(16):
    buttons[i].grid(row=i//4, column=i%4)

first_card = None
matches = 0

def click(i):
    global first_card, matches
    if buttons[i]['text'] == '?' and (first_card is None or i != first_card[1]):
        buttons[i].config(text=cards[i])
        if first_card is None:  # first card in the pair
            first_card = (cards[i], i)
        else:  # second card in the pair
            if cards[i] == first_card[0]:  # match
                matches += 1
                if matches == len(cards) // 2:  # all pairs found
                    messagebox.showinfo('Wygrana!', 'Udało Ci się odnaleźć wszystkie pary!')
                    root.quit()
            else:  # no match
                root.after(1000, hide, i, first_card[1])  # hide cards again after 1 second
            first_card = None

def hide(i, j):
    buttons[i].config(text='?')
    buttons[j].config(text='?')

for i in range(16):
    buttons[i]['command'] = lambda i=i: click(i)

root.mainloop()