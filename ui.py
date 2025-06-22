from tkinter import *
from constants import GRID_SIZE, CELL_SIZE
import time
from cell import create_world, update_world



def create_canvas(tk):
    canvas = Canvas(tk, width=500, height=500)
    for x in range(GRID_SIZE[0]):
        for y in range(GRID_SIZE[1]):
            canvas.create_rectangle(x * CELL_SIZE, y*CELL_SIZE, x*CELL_SIZE+CELL_SIZE, y*CELL_SIZE+CELL_SIZE, fill='black', outline='white')
   
    canvas.pack()

    return canvas
    
def update_canvas(canvas, world):
    for cell in world.values():
        canvas.itemconfig(cell.rect_id, fill = "white" if cell.alive else "black")






def step(canvas, iterations=5):

    current_iter = 0
    world = create_world(canvas)
    if current_iter < iterations:
       #global current_iter
        update_world(world)
        update_canvas(canvas, world)
        current_iter += 1
        print(f"iteration: {current_iter}")
        canvas.after(500, step, canvas)  # schedule next update after 500ms

def main(tk): 
    canvas = create_canvas(tk)
    iterations = 5  # total number of updates
    step(canvas, iterations)


if __name__ == "__main__":
    tk = Tk()
    main(tk)  # start the update loop
    tk.mainloop()