from ObstacleGrid import *
from AStar import *
import pygame as pg

class AStarVisualizer:
    def __init__(self, render):
        self.render = render
        self.a_star = AStar()
        self.grid = ObstacleGrid(render, 9, 16, 100, 100)

        self.running_simulation = False

        # Adds obstacles
        self.grid.toggle_obstacle(0, 1)

    def run_simulation(self):
        if self.run_simulation == True:
            return
        self.running_simulation = True

    
    def step(self):
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
        self.grid.toggle_obstacle(*grid_position)

    def draw(self):
        if self.running_simulation:
            self.step()
        self.grid.draw()