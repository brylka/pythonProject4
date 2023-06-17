import tkinter as tk
import random

# root window
root = tk.Tk()
root.title('Game of Life')

# game state
SIZE = 50
alive = {(i, j): random.choice([0, 1]) for i in range(SIZE) for j in range(SIZE)}

# game canvas
canvas = tk.Canvas(root, width=SIZE*10, height=SIZE*10, bg="white")
canvas.pack()

def update():
    global alive
    new_alive = {}
    for i in range(SIZE):
        for j in range(SIZE):
            alive_neighbors = sum(alive.get((i2, j2), 0)
                                  for i2 in range(i-1, i+2)
                                  for j2 in range(j-1, j+2)
                                  if (i2, j2) != (i, j))
            if alive[(i, j)] and alive_neighbors in {2, 3}:
                new_alive[(i, j)] = 1
            elif not alive[(i, j)] and alive_neighbors == 3:
                new_alive[(i, j)] = 1
            else:
                new_alive[(i, j)] = 0
    alive = new_alive

    # redraw
    canvas.delete('all')
    for (i, j), a in alive.items():
        if a:
            canvas.create_rectangle(j*10, i*10, (j+1)*10, (i+1)*10, fill='black')

    # schedule next update
    root.after(100, update)

update()
root.mainloop()