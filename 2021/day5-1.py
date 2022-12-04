"""Advent of Code 2021 - Challenge 5 Part 1"""

from typing import List

class Line:
    def __init__(self, x1, x2, y1, y2):
        self.slope = (y2-y1)/(x2-x1) if x1 != x2 else None
        self.intercept = y1 - (self.slope*x1) if self.slope else x1

    def contains_point(self, x,y):
        if self.slope:
            return y == self.slope*x + self.intercept # y = mx+b
        else:
            return x == self.intercept and y >=  # vertical line

# Get Input
with open("inputs/day5.txt", 'r') as file:
    raw_input = [line.strip() for line in file.readlines()]
    lines: List[Line] = []
    for line in raw_input:
        [p1, p2] = line.split(" -> ")
        [x1, y1] = p1.split(",")
        [x2, y2] = p2.split(",")
        lines.append(Line(
            int(x1),
            int(x2),
            int(y1),
            int(y2)
        ))

# create line diagram
vent_grid = [["." for _ in range(10)] for _ in range(10)]

for y, row in enumerate(vent_grid):
    for x, point in enumerate(row):
        for line in lines:
            if line.contains_point(x,y):
                vent_grid[y][x] += 1 if vent_grid[y][x] != "." else 1


for row in vent_grid:
    print(" ".join(row))

# check if lines overlap
# count number of overlapping lines