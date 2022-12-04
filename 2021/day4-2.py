"""Advent of Code 2021 - Challenge 4 Part 1"""

from typing import List
import numpy as np

# Get Input
with open("inputs/day4.txt", 'r') as file:
    raw_input = [line.strip() for line in file.readlines()]

def process_input(input: List[int]):
    number_order = [int(number) for number in input.pop(0).split(",")]
    boards = []
    for line in input:
        if not line: # newline
            boards.append([])
            continue
        board: List[List[int]] = boards[-1]
        board.append([])
        for number in line.split(" "):
            if number:
                board[-1].append(int(number))
    
    bingo_boards = [BingoBoard(board) for board in boards]
    return number_order, bingo_boards

class BingoBoard:

    def __init__(self, board):
        self.round = 0
        self.current_number = 0
        self.board = board
        self.selected_numbers = set()
        self.unselected_numbers = { n for row in self.board for n in row } # flatten list of numbers

    def play_number(self, number):
        self.round += 1
        self.current_number = number
        if number not in self.unselected_numbers:
            return
        self.unselected_numbers.remove(number)
        self.selected_numbers.add(number)

    def check_winner(self):
        for row in self.board:
            rowset = set(row)
            if rowset.issubset(self.selected_numbers):
                return True

        transposed_board = np.transpose(self.board)
        for row in transposed_board:
            rowset = set(row)
            if rowset.issubset(self.selected_numbers):
                return True
        return False

    def play_through(self, numbers):
        for number in numbers:
            self.play_number(number)
            if self.check_winner():
                return self
        return self

    def get_win_score(self):
        return sum(self.unselected_numbers) * self.current_number

number_order, bingo_boards = process_input(raw_input)

won_boards = [board.play_through(number_order) for board in bingo_boards]
won_boards.sort(key=lambda board: board.round)

print(won_boards[-1].get_win_score())
