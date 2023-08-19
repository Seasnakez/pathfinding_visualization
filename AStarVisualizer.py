import pygame as pg

class AStarVisualizer:
    def __init__(self, render, a_star, grid):
        self.render = render
        self.a_star = a_star
        self.grid = grid

    def draw(self):
        # Draw filled
        for y, row in enumerate(self.grid.get_grid()):
            for x, has_obstacle in enumerate(row):
                if has_obstacle:
                    color = pg.Color("grey")
                else:
                    color = pg.Color("white")
                pg.draw.rect(self.render.screen, color, pg.Rect(x * self.grid.cell_width, y * self.grid.cell_height, self.grid.cell_width, self.grid.cell_height))
                pg.draw.rect(self.render.screen, pg.Color("darkgray"), pg.Rect(x * self.grid.cell_width, y * self.grid.cell_height, self.grid.cell_width, self.grid.cell_height), 1)
        
        # All borders but the edges get drawn twice, to keep all borders equal size, a thicker border is drawn on the edges to compensate
        pg.draw.rect(self.render.screen, pg.Color("darkgray"), pg.Rect(0, 0, self.grid.width * self.grid.cell_width, self.grid.height * self.grid.cell_height), 2)