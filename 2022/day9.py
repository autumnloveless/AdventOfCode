"""Advent of Code 2022 - Challenge 9"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Vector2:
    x: int
    y: int

    def __add__(self, point: "Vector2"):
        """Add vector2 together """
        return Vector2(self.x + point.x, self.y + point.y)
    
    def __sub__(self, point: "Vector2"):
        """Add vector2 together """
        return Vector2(self.x - point.x, self.y - point.y)
    
    def _safe_divide(self, quotient, divisor):
        """Division, but divide by zero returns 0"""
        return divisor and quotient//divisor or divisor

    def normalized(self):
        return Vector2(self._safe_divide(self.x, abs(self.x)), self._safe_divide(self.y, abs(self.y)))
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

head_movement_dict = {
    "U": Vector2(0,1),  # up
    "D": Vector2(0,-1), # down
    "R": Vector2(1, 0), # right
    "L": Vector2(-1, 0)  # left 
}

def get_data(filename) -> list[list[str,str]]:
    """ load data from file """
    with open(filename, 'r') as file:
        inputs = [row.split(" ") for row in file.readlines()]
    return inputs

def calculate_movement(point_1: Vector2, point_2: Vector2) -> Vector2:
    """ Returns a vector2 with the movement of the following point """
    difference = (point_1 - point_2)
    if abs(difference.x) > 1 or abs(difference.y) > 1:
        return difference.normalized()
    return Vector2(0,0)

def count_unique_tail_movement(data: list[list[str, str]], number_of_knots: int) -> int:
    """ Calculate unique movement of tail given a number of total knots """
    # initial position
    visited_points = set()
    knots = [Vector2(0,0) for _ in range(number_of_knots)]
    visited_points.add(knots[-1])

    # move knots
    for direction, count in data:
        for _ in range(int(count)):
            knots[0] += head_movement_dict[direction]
            for index in range(1, len(knots)):
                knots[index] += calculate_movement(knots[index-1], knots[index])
            visited_points.add(knots[-1])

    # total unique points
    return len(visited_points)

if __name__ == "__main__":
    data = get_data("2022/inputs/day9.txt")
    print("Part 1", count_unique_tail_movement(data, 2))
    print("Part 2", count_unique_tail_movement(data, 10))
