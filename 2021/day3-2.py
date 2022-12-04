"""Advent of Code 2021 - Challenge 3 Part 2"""

from typing import List
import numpy as np

# Get Input
with open("inputs/day3.txt", 'r') as file:
    input = [list(line.strip()) for line in file.readlines()]
    processed_input = ["".join(column) for column in np.transpose(input) ]

def get_most_common_bit(bits: str):
    return "0" if bits.count('0') > len(bits)/2 else "1"

def get_least_common_bit(bits: str):
    return "0" if bits.count('0') <= len(bits)/2 else "1"

# Part 1 ---------------

gamma_rate = ""
epsilon_rate = ""
for column in processed_input:
    most_common_bit =  get_most_common_bit(column)
    gamma_rate += most_common_bit
    epsilon_rate += "0" if most_common_bit == "1" else "1"

power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
print("Power consumption: ", power_consumption)

# Part 2 ---------------

filtered_rows = input
column_index = 0
while len(filtered_rows) > 1:
    column = "".join([row[column_index] for row in filtered_rows])
    most_common_bit = get_most_common_bit(column)
    filtered_rows = [row for row in filtered_rows if row[column_index] == most_common_bit]
    column_index += 1
oxygen_rating = "".join(filtered_rows[0])

filtered_rows = input
column_index = 0
while len(filtered_rows) > 1:
    column = "".join([row[column_index] for row in filtered_rows])
    most_common_bit = get_least_common_bit(column)
    filtered_rows = [row for row in filtered_rows if row[column_index] == most_common_bit]
    column_index += 1
co2_rating = "".join(filtered_rows[0])


life_support_rating =  int(oxygen_rating, 2) * int(co2_rating, 2)
print("Life support rating: ", life_support_rating)