"""Advent of Code 2022 - Challenge 3 Part 2"""

from typing import List
import string

# Get Input
with open("inputs/day3.txt", 'r') as file:
    input = [line.strip() for line in file.readlines()]


character_values = { character: index+1 for index, character in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

def get_shared_item(rucksack_1_set, rucksack_2_set, rucksack_3_set):
    return rucksack_1_set & rucksack_2_set & rucksack_3_set

# for each rucksack
total_priority_value = 0
index = 0
while index < len(input):
    # convert item list to set for efficient computation
    rucksack_sets = [set(character) for character in input[index:index+3]]

    # find shared value in group
    shared_character_set = set.intersection(*rucksack_sets)
    if shared_character_set:
        shared_character = shared_character_set.pop()
        total_priority_value += character_values[shared_character] # add priority value
    index += 3 # move to next group

print(total_priority_value)