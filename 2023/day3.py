"""Advent of Code 2023 - Challenge 3"""
import re
from typing import Optional
from dataclasses import dataclass

@dataclass
class Number:
    row_index: int
    col_start: int
    col_stop: int
    value: int

def get_data(filename) -> list[str]:
    """ load data from file """
    with open(filename, 'r') as file:
        inputs = [line.strip() for line in file.readlines()]
    return inputs

def parse_numbers(data: list[str]) -> list[Number]:
    """ Given a list of strings, returns a list of every number found, including row index, and start and end column index """
    numbers = []
    for row_index, row in enumerate(data):
        numbers += [Number(row_index, match.start(), match.end(), int(data[row_index][match.start():match.end()])) for match in re.finditer(r'\d+', row)]
    return numbers

def find_adjacent_part(data: list[str], number: Number, symbol: str = None) -> Optional[tuple[int,int]]:
    """ Determine if there is a symbol adjacent to this number. Returns the row and column if a match is found. 
        If a symbol is provided, only that symbol is considered. """
    for row in range(max(0, number.row_index-1), min(number.row_index+2, len(data))):
        for column in range(max(0, number.col_start-1), min(number.col_stop+1, len(data))):
            if (not symbol and data[row][column] not in "0123456789.") or (symbol and data[row][column] == symbol):
                return row, column
    return None

def get_adjacent_parts(numbers: list[Number], data: list[str], symbol: str=None) -> dict[tuple, list[Number]]:
    """ Returns a dictionary of parts that are adjacent to symbols. symbol_index: list[Number]. 
        If a symbol type is provided, only that symbol is considered. """
    part_numbers: dict[tuple, list[Number]] = {}
    for number in numbers:
        adjacent_part = find_adjacent_part(data, number, symbol)
        if adjacent_part is not None:
            part_numbers.setdefault(adjacent_part, [])
            part_numbers[adjacent_part].append(number)
    return part_numbers

def part_1(data: list[str]):
    """ Returns a sum of all numbers that have a symbol adjacent to them """    
    numbers = parse_numbers(data) # get all numbers, including start and stop indexes
    part_numbers = get_adjacent_parts(numbers, data) # get all numbers that are adjacent to any symbol
    return sum(number.value for numbers in part_numbers.values() for number in numbers ) # return sum

def part_2(data: list[str]):
    """ Returns a sum of the product of all pairs of numbers with a star symbol connecting them """    
    numbers = parse_numbers(data) # get all numbers, including start and stop indexes
    part_numbers = get_adjacent_parts(numbers, data, "*") # get all numbers that are adjacent to the star symbol
    return sum(numbers[0].value * numbers[1].value for numbers in part_numbers.values() if len(numbers) == 2 ) # return sum of product of pairs

if __name__ == "__main__":
    data = get_data("2023/inputs/sample-input.txt")
    data = get_data("2023/inputs/day3.txt")
    print("Part 1", part_1(data))
    print("Part 2", part_2(data))
