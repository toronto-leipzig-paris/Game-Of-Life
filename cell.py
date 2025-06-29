class Cell:
    def __init__(self, alive, position, cell_size):
        self.previously_alive = alive
        self.alive = alive
        self.position = position
        self.cell_size = cell_size
        x, y = position
        self.neighbor_positions = [
            (x + cell_size, y),
            (x - cell_size, y),
            (x, y + cell_size),
            (x, y - cell_size),
            (x + cell_size, y + cell_size),
            (x - cell_size, y - cell_size),
            (x - cell_size, y + cell_size),
            (x + cell_size, y - cell_size),
        ]

    def interact(self, cells):
        alive_neighbors = {
            id: cell
            for id, cell in cells.items()
            if cell.position in self.neighbor_positions and cell.previously_alive
        }
        if len(alive_neighbors) < 2 or len(alive_neighbors) > 3:
            self.previously_alive = self.alive
            self.alive = False
        if not self.previously_alive and len(alive_neighbors) == 3:
            self.previously_alive = self.alive
            self.alive = True
