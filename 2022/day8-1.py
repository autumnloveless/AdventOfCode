"""Advent of Code 2022 - Challenge 8 Part 1"""

from dataclasses import dataclass
from typing import List, Union, Optional, Dict

# Get Input
with open("inputs/day8.txt", 'r') as file:
    input = [[num for num in line.strip()] for line in file.readlines()]

width = len(input[0])
height = len(input)

def visible_from_up(row_index, col_index):
    for index in range(0, row_index):
        if input[index][col_index] >= input[row_index][col_index]:
            return False
    return True

def visible_from_down(row_index, col_index):
    for index in range(height-1, row_index, -1):
        if input[index][col_index] >= input[row_index][col_index]:
            return False
    return True

def visible_from_left(row_index, col_index):
    for index in range(0, col_index):
        if input[row_index][index] >= input[row_index][col_index]:
            return False
    return True

def visible_from_right(row_index, col_index):
    for index in range(width-1, col_index, -1):
        if input[row_index][index] >= input[row_index][col_index]:
            return False
    return True


def check_if_visible(row_index, col_index):
    is_visible_up = visible_from_up(row_index, col_index)   
    is_visible_down = visible_from_down(row_index, col_index)   
    is_visible_left = visible_from_left(row_index, col_index)   
    is_visible_right = visible_from_right(row_index, col_index)   

    return (is_visible_up or is_visible_down or is_visible_left or is_visible_right)


# determine visible trees
visible_from_outside = 0

for row_index, row in enumerate(input):
    if row_index in (0, len(input)-1): # add top and bottom rows of grid
        visible_from_outside += len(row)
        continue
    
    for col_index, col in enumerate(row):
        if col_index in (0, len(row)-1): # add columns on sides of grid
            visible_from_outside += 1
            continue

        if check_if_visible(row_index, col_index):
            visible_from_outside += 1

print(visible_from_outside)