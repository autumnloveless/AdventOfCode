"""Advent of Code 2022 - Challenge 5 Part 2"""

from typing import List

# Get Input
with open("inputs/day5.txt", 'r') as file:
    input = [line.replace("\n","") for line in file.readlines()]
    
# Data setup ==========================
finished_crates = False

# crates
crates_lines = []
instructions_raw = []
for line in input:
    if not line:
        finished_crates = True
    elif not finished_crates:
        crates_lines.append(line)
    else:
        instructions_raw.append(line)

crate_numbers = [int(number) for number in crates_lines.pop().split(" ") if number != ""]

crates = [[] for _ in range(crate_numbers[-1])]

for line in reversed(crates_lines):
    index = 0
    while index < (len(line)-1)/4:
        crate_spot = line[(index*4)+1]
        if crate_spot.isalpha():
            crates[index].append(crate_spot)
        index += 1
            
instructions = [[int(word) for word in instruction.split(" ") if word.isnumeric()] for instruction in instructions_raw]

# Logic ==========================

for instruction in instructions:
    [quantity, from_container, to_container] = instruction
    moved_crates = [ crates[from_container-1].pop() for i in range(quantity) ]
    for crate in reversed(moved_crates):
        crates[to_container-1].append(crate)

final_output = ""
for column in crates:
    final_output += column[-1]

print(final_output)