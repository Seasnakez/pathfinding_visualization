from ObstacleGrid import *
from AStarVisualizer import *
from AStar import *
import pygame as pg

class SoftwareRenderer:
    def __init__(self) -> None:
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

        self.a_star = AStar()
        self.grid = ObstacleGrid(3, 5, 100, 100)
        self.a_star_visualizer = AStarVisualizer(self, self.a_star, self.grid)

    def draw(self):
        self.screen.fill(pg.Color("darkslategray"))
        self.a_star_visualizer.draw()

    def run(self):
        # Adds obstacles
        self.grid.toggle_obstacle(0, 1)

        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
    

if __name__ == "__main__":
    app = SoftwareRenderer()
    app.run()