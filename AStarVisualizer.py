from ObstacleGrid import *
from AStar import *
import pygame as pg

class AStarVisualizer:
    def __init__(self, render):
        self.render = render
        self.a_star = AStar()
        self.grid = ObstacleGrid(render, 3, 5, 100, 100)

        # Adds obstacles
        self.grid.toggle_obstacle(0, 1)

    def draw(self):
        self.grid.draw()