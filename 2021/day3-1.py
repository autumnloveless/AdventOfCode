"""Advent of Code 2021 - Challenge 3 Part 1"""

from typing import List

# Get Input
with open("inputs/day3.txt", 'r') as file:
    input = [line.strip() for line in file.readlines()]

bit_count = [ [0,0] for _ in range(len(input[0])) ]
for row in input:
    for index, bit in enumerate(row):
        bit_count[index][int(bit)] += 1 # 0 or 1

gamma_rate = ""
for column in bit_count:
    gamma_rate += "0" if column[0] > column[1] else "1"

epsilon_rate = "".join(["0" if b=="1" else "1" for b in gamma_rate])

print(int(gamma_rate, 2) * int(epsilon_rate, 2))