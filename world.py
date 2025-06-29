from numpy import random

from cell import Cell
from constants import GRID_SIZE


class World:
    def __init__(
        self,
        grid_size=GRID_SIZE,
        window_size=800,  # pixels
    ):
        self.width, self.height = grid_size
        self.cell_size = window_size // max(self.width, self.height)
        self.create_canvas()

    def create_canvas(self):
        from tkinter import Canvas

        self.canvas = Canvas(
            width=self.width * self.cell_size,
            height=self.height * self.cell_size,
        )

        self.canvas.pack()
        for x in range(self.width):
            for y in range(self.height):
                self.canvas.create_rectangle(
                    x * self.cell_size,
                    y * self.cell_size,
                    x * self.cell_size + self.cell_size,
                    y * self.cell_size + self.cell_size,
                    outline="white",
                )

    def spawn_cells(self):
        self.cells = {
            id: Cell(
                random.choice([True, False], p=[0.2, 0.8]),
                tuple(self.canvas.coords(id)[:2]),
                self.cell_size,
            )
            for id in self.canvas.find_all()
        }

    def update_canvas(self):
        for id, cell in self.cells.items():
            if cell.alive and not cell.previously_alive:
                color = "green"
            elif cell.alive and cell.previously_alive:
                color = "white"
            elif not cell.alive and cell.previously_alive:
                color = "red"
            elif not cell.alive and not cell.previously_alive:
                color = "black"
            self.canvas.itemconfig(id, fill=color)
        self.canvas.update()

    def step(self):
        for cell in self.cells.values():
            cell.interact(self.cells)
        self.update_canvas()

    def print_live_cells(self):
        live_cells = [cell for cell in self.cells.values() if cell.alive]
        print(f"Live cells: {len(live_cells)}")
        for cell in live_cells:
            print(f"Cell at {cell.position} is alive.")

    def run(self):
        import time

        self.spawn_cells()
        while True:
            self.step()
            time.sleep(0.5)
