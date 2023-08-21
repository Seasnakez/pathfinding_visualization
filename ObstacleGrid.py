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

    def adjacent(self, row, column, include_obstacles=False, cardinal_directions=True):
        adjacent_list = []
        # Top left
        if row-1 >= 0 and column-1 >= 0 and not cardinal_directions:
            adjacent_list.append((row-1, column-1))
        # Top middle
        if row-1 >= 0:
            adjacent_list.append((row-1, column))
        # Top right
        if row-1 >= 0 and column+1 <= self.width-1 and not cardinal_directions:
            adjacent_list.append((row-1, column+1))
        # Right
        if column-1 >= 0:
            adjacent_list.append((row, column-1))
        # Left
        if column+1 <= self.width-1:
            adjacent_list.append((row, column+1))
        # Bottom left
        if row+1 <= self.height-1 and column-1 >= 0 and not cardinal_directions:
            adjacent_list.append((row+1, column-1))
        # Bottom middle
        if row+1 <= self.height-1:
            adjacent_list.append((row+1, column))
        # Bottom rights
        if row+1 <= self.height-1 and column+1 <= self.width-1 and not cardinal_directions:
            adjacent_list.append((row+1, column+1))


        if not include_obstacles:
            temp = []
            for row, column in adjacent_list:
                if self.obstacle_map[row][column] == 0:
                    temp.append((row, column))
            adjacent_list = temp
        return adjacent_list

    def change_color(self, row, column, color):
        self.color_map[row][column] = color

    def reset_colors(self):
        for row, content in enumerate(self.obstacle_map):
            for column, has_obstacle in enumerate(content):
                if has_obstacle:
                    color = pg.Color("gray")
                else:
                    color = pg.Color("white")
                self.color_map[row][column] = color

    def toggle_obstacle(self, row, column):
        if self.obstacle_map[row][column] == 0:
            self.obstacle_map[row][column] = 1
            self.color_map[row][column] = pg.Color("gray")
        else:
            self.obstacle_map[row][column] = 0
            self.color_map[row][column] = pg.Color("white")
        
    def world_to_grid(self, x, y):
        if y > self.height * self.cell_height or x > self.width * self.cell_width:
            return None
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