from ObstacleGrid import *
from AStar import *
import pygame as pg

class AStarVisualizer:
    def __init__(self, render):
        self.render = render
        self.grid = ObstacleGrid(render, 9, 16, 100, 100)
        self.goal = (self.grid.height-1, self.grid.width-1)
        self.start = (0, 0)
        self.reset_colors()
        self.running_simulation = False
        self.last_grid_position = self.start

    def reset_colors(self):
        if self.run_simulation == True:
            return
        self.grid.reset_colors()
        self.grid.change_color(*self.goal, pg.Color("green"))
        self.grid.change_color(*self.start, pg.Color("black"))

    def run_simulation(self):
        if self.run_simulation == True:
            return
        self.running_simulation = True
        self.reset_colors()
        self.a_star = AStar(self.start, self.goal, self.grid.adjacent)

    def step(self):
        open, closed, path = self.a_star.step()
        for position in open:
            if position != self.start and position != self.goal:
                self.grid.change_color(*position, pg.Color("aquamarine3"))
        for position in closed:
            if position != self.start and position != self.goal:
                self.grid.change_color(*position, pg.Color("aquamarine4"))

        if path:
            for position in path:
                if position != self.start and position != self.goal:
                    self.grid.change_color(*position, pg.Color("lightgreen"))
            print("finished")
            self.running_simulation = False

    def mouse_pressed(self, position):
        if self.running_simulation:
            return
        grid_position = self.grid.world_to_grid(*position)
        if self.last_grid_position != grid_position:
            if grid_position == None:
                return
            self.last_grid_position = grid_position
            if grid_position == self.start or grid_position == self.goal:
                return
            self.grid.toggle_obstacle(*grid_position)


    def draw(self):
        if self.running_simulation:
            self.step()
        self.grid.draw()