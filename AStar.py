import math

class AStarNode:
    def __init__(self, g, h, parent, position):
        self.g = g
        self.h = h
        self.parent = parent
        self.position = position

    def cost(self):
        return self.g + self.h


class AStar:
    def __init__(self, start, goal, get_neighbours):
        self.start = start
        self.goal = goal
        self.get_neighbours = get_neighbours

        self.open = [AStarNode(0, self.cost_heuristic(self.start), None, self.start)]
        self.closed = []

    def step(self):
        # Picks lowest cost node in open
        current = self.open[0]
        for node in self.open:
            if node.cost() < current.cost():
                current = node

        # If open set is empty, there is no valid path to the goal
        if not self.open: path = [] 
        else: path = None
        if current.position == self.goal:
            path = self.reconstruct(current)
            print(path)
        else:
            self.open.remove(current)
            self.closed.append(current)
            for neighbour in self.get_neighbours(*current.position):
                cost = current.g + 1

                in_open = False
                in_closed = False

                # if neighbour already exists in open and is more expensive, it's inferior and is removed
                node = self.get_by_position(neighbour, self.open)
                if node:
                    in_open = True
                    if cost < node.g:
                        self.open.remove(node)
                # if neighbour already exists in closed and is more expensive, it's inferior and is removed
                node = self.get_by_position(neighbour, self.closed)
                if node:
                    in_closed = True
                    if cost < node.g:
                        self.closed.remove(node)
                
                if not in_open and not in_closed:
                    new_node = AStarNode(cost, self.cost_heuristic(neighbour), current, neighbour)
                    self.open.append(new_node)
                
        return self.convert_to_positions(self.open), self.convert_to_positions(self.closed), path
    
    def convert_to_positions(self, set):
        position_list = []
        for node in set:
            position_list.append(node.position)
        return position_list

    def get_by_position(self, position, set):
        for node in set:
            if node.position == position:
                return node
        return None

    def cost_heuristic(self, position):
        return math.sqrt((position[0] - self.goal[0])**2 + (position[1] - self.goal[1])**2) * 10

    def reconstruct(self, node):
        current = node
        path = [current.position]
        while current.parent != None:
            path.append(current.parent.position)
            current = current.parent
        path.reverse()
        return path

