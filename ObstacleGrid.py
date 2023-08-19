class ObstacleGrid:
    def __init__(self, width, height, cell_width, cell_height):
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

        def adjacent(self, include_obstacles=True):
            pass

        def toggle_obstacle(x, y):
            if self.grid[y][x] == 0:
                self.grid[y][x] = 1
            else:
                self.grid[y][x] = 0
            
        def world_to_grid(x, y):
            pass

        def grid_to_world(x, y):
            pass

        def get_grid(self):
            return self.grid
