import tkinter as tk
from tkinter import messagebox
import random

# root window
root = tk.Tk()
root.geometry("400x300")
root.resizable(False, False)
root.title('Kamień, Papier, Nożyce')

choices = ['Kamień', 'Papier', 'Nożyce']

player_score = 0
computer_score = 0

def play(user_choice):
    global player_score
    global computer_score
    comp_choice = random.choice(choices)
    result = ''

    if user_choice == comp_choice:
        result = 'Remis!'
    elif (user_choice == 'Kamień' and comp_choice == 'Nożyce') or \
        (user_choice == 'Nożyce' and comp_choice == 'Papier') or \
        (user_choice == 'Papier' and comp_choice == 'Kamień'):
        result = 'Wygrałeś!'
        player_score += 1
    else:
        result = 'Przegrałeś!'
        computer_score += 1

    result_text.set(f"Komputer wybrał: {comp_choice}\n{result}")
    score_text.set(f"Gracz: {player_score} Komputer: {computer_score}")

# buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Kamień", command=lambda: play('Kamień'))
rock_button.pack(side='left', padx=10)

paper_button = tk.Button(button_frame, text="Papier", command=lambda: play('Papier'))
paper_button.pack(side='left', padx=10)

scissors_button = tk.Button(button_frame, text="Nożyce", command=lambda: play('Nożyce'))
scissors_button.pack(side='left', padx=10)

# result
result_text = tk.StringVar()

result_label = tk.Label(root, textvariable=result_text)
result_label.pack(pady=20)

# score
score_text = tk.StringVar()

score_label = tk.Label(root, textvariable=score_text)
score_label.pack(pady=20)

root.mainloop()