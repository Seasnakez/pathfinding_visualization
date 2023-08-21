import pygame as pg

class ObstacleGrid:
    def __init__(self, render, height, width, cell_width, cell_height):
        self.render = render
        self.obstacle_map = [[0 for _ in range(width)] for _ in range(height)]
        self.color_map = [[pg.Color("white") for _ in range(width)] for _ in range(height)]
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.height = height
        self.width = width

    def adjacent(self, include_obstacles=True):
        pass

    def toggle_obstacle(self, row, column):
        if self.obstacle_map[row][column] == 0:
            self.obstacle_map[row][column] = 1
            self.color_map[row][column] = pg.Color("gray")
        else:
            self.obstacle_map[row][column] = 0
            self.color_map[row][column] = pg.Color("white")
        
    def world_to_grid(self, x, y):
        return (y // self.cell_height, x // self.cell_width)

    def grid_to_world(self, row, column):
        return (column * self.cell_width, row * self.cell_height)

    def get_grid(self):
        return self.obstacle_map

    def draw(self):
        for y, row in enumerate(self.color_map):
            for x, color in enumerate(row):
                # Draw filled square
                pg.draw.rect(self.render.screen, color, pg.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height))
                # Draw border
                pg.draw.rect(self.render.screen, pg.Color("darkgray"), pg.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height), 1)
        
        # All borders but the edges get drawn twice, to keep all borders equal size, a thicker border is drawn on the edges to compensate
        pg.draw.rect(self.render.screen, pg.Color("darkgray"), pg.Rect(0, 0, self.width * self.cell_width, self.height * self.cell_height), 2)