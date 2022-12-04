"""Advent of Code 2022 - Challenge 4 Part 1"""

from typing import List

# Get Input
with open("inputs/day4.txt", 'r') as file:
    input = [line.strip() for line in file.readlines()]

contains_count = 0

for section_list in input:
    [elf1, elf2] = section_list.split(",")
    [elf1_start, elf1_end] = elf1.split("-")
    [elf2_start, elf2_end] = elf2.split("-")

    elf1_range = set(range(int(elf1_start),int(elf1_end)+1))
    elf2_range = set(range(int(elf2_start),int(elf2_end)+1))

    if len(elf1_range & elf2_range) > 0:
        contains_count += 1

print(contains_count)

