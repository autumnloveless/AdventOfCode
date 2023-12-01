"""Advent of Code 2022 - Challenge 9"""
from typing import Optional
from dataclasses import dataclass

def get_data(filename) -> list[list[str,str]]:
    """ load data from file """
    with open(filename, 'r') as file:
        inputs = [row.split(" ") if row.startswith("addx") else [row, None] for row in file.readlines()]
    return inputs

def part_1(data: list[str, Optional[str]]):
    cycle = 1
    current_value = 1
    total_value = 0

    for instruction, add_value in data:
        if (cycle + 20) % 40 == 0:
            total_value += cycle * current_value

        if instruction.strip() == "noop":
            cycle += 1
            continue
        
        cycle += 1
        if (cycle + 20) % 40 == 0:
            total_value += cycle * current_value
        
        cycle += 1
        current_value += int(add_value)

    return total_value


def part_2(data: list[str, Optional[str]]):
    cycle = 1
    x_register = 1

    for instruction, add_value in data:
        if (cycle-1) % 40 == 0:
            print("")
        print("#" if abs(((cycle-1) % 40) - x_register) < 2 else ".", end="")

        if instruction.strip() == "noop":
            cycle += 1
            continue
        
        cycle += 1
        if (cycle-1) % 40 == 0:
            print("")
        print("#" if abs(((cycle-1) % 40) - x_register) < 2 else ".", end="")
        
        x_register += int(add_value)
        cycle += 1


if __name__ == "__main__":
    data = get_data("2022/inputs/day10.txt")
    # data = get_data("2022/inputs/sample-input.txt")
    print("Part 1", part_1(data))
    part_2(data)
