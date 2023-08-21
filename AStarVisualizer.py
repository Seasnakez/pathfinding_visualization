from ObstacleGrid import *
from AStar import *
import pygame as pg

class AStarVisualizer:
    def __init__(self, render):
        self.render = render
        self.grid = ObstacleGrid(render, 9, 16, 100, 100)
        self.goal = (self.grid.height-1, self.grid.width-1)
        self.grid.change_color(*self.goal, pg.Color("green"))
        self.start = (0, 0)
        self.grid.change_color(*self.start, pg.Color("black"))
        self.a_star = AStar(self.start, self.goal)
        self.running_simulation = False

    def run_simulation(self):
        if self.run_simulation == True:
            return
        self.running_simulation = True

    
    def step(self):
        if not self.running_simulation:
            return
        pass
        """
        frontier ... = self.a_star.step()
        for row, column in frontier:
            grid.update_color(row, column, color.yellow)
        etc for each list

        """
        
        # Update color map according to step output

    def mouse_pressed(self, position):
        if self.running_simulation:
            return
        grid_position = self.grid.world_to_grid(*position)
        if grid_position == None:
            return
        if grid_position == self.start or grid_position == self.goal:
            return
        self.grid.toggle_obstacle(*grid_position)

    def draw(self):
        if self.running_simulation:
            self.step()
        self.grid.draw()