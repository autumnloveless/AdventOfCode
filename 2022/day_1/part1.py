"""Advent of Code 2022 - Challenge 1 Part 1"""

from typing import List

# Get Input
with open("input.txt", 'r') as file:
    input = file.readlines()

# Setup data
elves: List[int] = [0]

# Calcuate calories
for line in input:
    if line != "\n":
        elves[-1] += int(line)
    else:
        elves.append(0)

elves.sort(reverse=True)
print(elves[0]) # part 1 - largest elf
print(sum(elves[0:3])) # part 2 - sum of largest 3