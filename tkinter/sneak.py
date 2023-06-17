import tkinter as tk
import random

# root window
root = tk.Tk()
root.title('Snake')

# game state
SIZE = 20
snake = [(SIZE // 2, SIZE // 2)]
direction = 'right'
food = None

# game canvas
canvas = tk.Canvas(root, width=SIZE*10, height=SIZE*10, bg="black")
canvas.pack()

def move_snake():
    global snake, food, direction
    # compute next position
    head = snake[0]
    if direction == 'up':
        new_head = (head[0] - 1, head[1])
    elif direction == 'down':
        new_head = (head[0] + 1, head[1])
    elif direction == 'left':
        new_head = (head[0], head[1] - 1)
    else:  # direction == 'right'
        new_head = (head[0], head[1] + 1)
    # check if game is over
    if new_head in snake or new_head[0] < 0 or new_head[0] >= SIZE or new_head[1] < 0 or new_head[1] >= SIZE:
        return  # game over
    # add new head
    snake = [new_head] + snake
    # check if food is eaten
    if new_head == food:
        food = None  # eat food
    else:
        snake.pop()  # remove tail
    # generate new food if needed
    if food is None:
        while True:
            food = (random.randint(0, SIZE-1), random.randint(0, SIZE-1))
            if food not in snake:
                break
    # redraw
    canvas.delete('all')
    for i, (x, y) in enumerate(snake):
        color = 'green' if i == 0 else 'white'  # make head green
        canvas.create_rectangle(y*10, x*10, (y+1)*10, (x+1)*10, fill=color)
    canvas.create_rectangle(food[1]*10, food[0]*10, (food[1]+1)*10, (food[0]+1)*10, fill='red')  # draw food
    # schedule next move
    root.after(100, move_snake)

def change_direction(new_direction):
    global direction
    direction = new_direction

root.bind('<Up>', lambda e: change_direction('up'))
root.bind('<Down>', lambda e: change_direction('down'))
root.bind('<Left>', lambda e: change_direction('left'))
root.bind('<Right>', lambda e: change_direction('right'))

move_snake()
root.mainloop()