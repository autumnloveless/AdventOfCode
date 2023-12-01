"""Advent of Code 2023 - Challenge 1"""
import re

def get_data(filename) -> list[list[str,str]]:
    """ load data from file """
    with open(filename, 'r') as file:
        inputs = file.readlines()
    return inputs

def part_1(data: list[str]):
    total = 0
    for row in data:
        digits = re.findall(r"\d", row)
        total += int(f"{digits[0]}{digits[-1]}")
    return total

valid_numbers = {
    "one": 1, 
    "two": 2, 
    "three": 3, 
    "four": 4, 
    "five": 5, 
    "six": 6, 
    "seven": 7, 
    "eight": 8, 
    "nine": 9
}

def part_2(data: list[str]):
    total = 0
    for row in data:
        digits = []
        for index in range(len(row)):
            if row[index].isdigit():
                digits.append(row[index])
                continue
            for string_number, value in valid_numbers.items():
                if row[index:].startswith(string_number):
                    digits.append(int(value))
                    break
        total += int(f"{digits[0]}{digits[-1]}")
    return total

if __name__ == "__main__":
    data = get_data("2023/inputs/day1.txt")
    # data = get_data("2023/inputs/sample-input.txt")
    print("Part 1", part_1(data))
    print("Part 2", part_2(data))
