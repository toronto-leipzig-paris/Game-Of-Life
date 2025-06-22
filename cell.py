from constants import GRID_SIZE
import random

class Cell:
    def __init__(self, alive, position, rect_id):
        self.previously_alive = alive
        self.alive = alive 
        self.position = position
        self.rect_id = rect_id
        x, y = position
        self.neighbor_positions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]
    
    def interaction(self, world):
        cell_neighbors = {position: cell for position, cell in world.items() if position in self.neighbor_positions}
        alive_neighbors = {position: cell for position, cell in cell_neighbors.items() if cell.previously_alive}

        if len(alive_neighbors) < 2 or len(alive_neighbors) > 3:
            self.previously_alive = self.alive
            self.alive = False
        if self.previously_alive == False and len(alive_neighbors) == 3:
            self.previously_alive = self.alive
            self.alive = True

def create_world(canvas):
    rect_ids = canvas.find_all()
    positions = {rect_id: tuple(canvas.coords(rect_id)[:2]) for rect_id in rect_ids}
    world = {position: Cell(random.choice([True, False]), position, rect_id) for rect_id, position in positions.items()}
    return world

def update_world(world):
    for position, cell in world.items():
        cell.interaction(world)