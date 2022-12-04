"""Advent of Code 2022 - Challenge 3 Part 1"""

from typing import List
import string

# Get Input
with open("inputs/day3.txt", 'r') as file:
    input = file.readlines()


character_values = { character: index+1 for index, character in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

def get_shared_item(compartment_1, compartment_2_set):
    for character in compartment_1:
        if character in compartment_2_set:
            return character
    return False

# for each rucksack
total_priority_value = 0
for rucksack in input:

    # divide in half - 2 compartments
    compartment_1 = rucksack[:len(rucksack)//2]
    compartment_2 = rucksack[len(rucksack)//2:]
    compartment_2_set = { character for character in compartment_2} # use set for efficient lookups

    character = get_shared_item(compartment_1, compartment_2_set)
    total_priority_value += character_values[character] if character else 0


print(total_priority_value)