class ObstacleGrid:
    def __init__(self, height, width, cell_width, cell_height):
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.height = height
        self.width = width

    def adjacent(self, include_obstacles=True):
        pass

    def toggle_obstacle(self, y, x):
        if self.grid[y][x] == 0:
            self.grid[y][x] = 1
        else:
            self.grid[y][x] = 0
        
    def world_to_grid(self, y, x):
        return (y // self.cell_height, x // self.cell_width)

    def grid_to_world(self, y, x):
        return (y * self.cell_height, x * self.cell_width)

    def get_grid(self):
        return self.grid
