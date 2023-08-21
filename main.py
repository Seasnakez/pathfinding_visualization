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

        self.a_star_visualizer = AStarVisualizer(self)

    def draw(self):
        self.screen.fill(pg.Color("darkslategray"))
        self.a_star_visualizer.draw()

    def run(self):
        while True:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT: 
                    exit()
                if event.type == pg.MOUSEBUTTONUP:
                    self.a_star_visualizer.mouse_pressed(pg.mouse.get_pos())
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.a_star_visualizer.run_simulation()
            self.draw()
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
    

if __name__ == "__main__":
    app = SoftwareRenderer()
    app.run()