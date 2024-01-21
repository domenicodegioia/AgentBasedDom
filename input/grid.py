import math
from random import randrange


class Grid:
    def __init__(self):
        # pick N random cells as obstacles
        obstacles = []
        for _ in range(10):
            obstacles.append((randrange(100), randrange(100)))
        self.obstacles = set(obstacles)

    def straight_line_distance(self, start, end):
        x_start, y_start = start
        x_end, y_end = end
        return math.sqrt((x_start - x_end) ** 2 + abs(y_start - y_end) ** 2)
        # Manhattan Distance = | x_1 − x_2 | + | y_1 − y_2 |
        # return abs(x_start - x_end) + abs(y_start - y_end)
