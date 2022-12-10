"""Advent of Code 2022 - Challenge 8 Part 2"""

from dataclasses import dataclass
from typing import List, Union, Optional, Dict

# Get Input
with open("inputs/day8.txt", 'r') as file:
    input = [[num for num in line.strip()] for line in file.readlines()]

width = len(input[0])
height = len(input)

def visible_from_up(row_index, col_index):
    count = 0
    for index in range(row_index-1, -1, -1):
        if input[index][col_index] >= input[row_index][col_index]:
            count += 1
            return count
        count += 1
    return count

def visible_from_down(row_index, col_index):
    count = 0
    for index in range(row_index+1, height):
        if input[index][col_index] >= input[row_index][col_index]:
            count += 1
            return count
        count += 1
    return count

def visible_from_left(row_index, col_index):
    count = 0
    for index in range(col_index-1, -1, -1):
        if input[row_index][index] >= input[row_index][col_index]:
            count += 1
            return count
        count += 1
    return count

def visible_from_right(row_index, col_index):
    count = 0
    for index in range(col_index+1, width):
        if input[row_index][index] >= input[row_index][col_index]:
            count += 1
            return count
        count += 1
    return count


def count_visible(row_index, col_index):
    visible_up = visible_from_up(row_index, col_index)   
    visible_down = visible_from_down(row_index, col_index)   
    visible_left = visible_from_left(row_index, col_index)   
    visible_right = visible_from_right(row_index, col_index)   

    return (visible_up * visible_down * visible_left * visible_right)


# determine visible trees
visible_list = []

for row_index, row in enumerate(input):
    for col_index, col in enumerate(row):

        score = count_visible(row_index, col_index)
        visible_list.append([row_index,col_index,score])

visible_list.sort(key=lambda x: x[2])
print(visible_list[-1][2])