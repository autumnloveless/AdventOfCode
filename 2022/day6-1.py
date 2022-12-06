"""Advent of Code 2022 - Challenge 6 Part 1"""

from typing import List

# Get Input
with open("inputs/day6.txt", 'r') as file:
    input = [line.strip() for line in file.readlines()][0]

def is_unique(substring):
    set = { c for c in substring }
    return len(set) == 4

index = 3
while index < len(input):
    if is_unique(input[index-3:index+1]):
        print(index+1)
        break
    index += 1
