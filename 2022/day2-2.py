"""Advent of Code 2022 - Challenge 2 Part 2"""

from typing import List

# Get Input
with open("inputs/day2.txt", 'r') as file:
    input = file.readlines()

# Setup data
choice_value = {
    "A": 1, # rock
    "B": 2, # paper
    "C": 3  # sissor
}

fight_value = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

winning_move = {
    "A": "C", # rock beats sissor
    "B": "A", # paper beats rock
    "C": "B" # sissor beats paper
}
losing_move = { value: key for key,value in winning_move.items() } # flip the winning_move dict, for losers

def determine_move(opponent_choice, result) -> str:
    if result == "X":
        return winning_move[opponent_choice] # I lose
    if result == "Y":
        return opponent_choice # I tie
    else:
        return losing_move[opponent_choice] # I win
    

# Determine score
score = 0
for line in input:
    [opponent_choice, result] = line.strip().split(" ") # process input
    
    my_choice = determine_move(opponent_choice, result) # determine move
    round_score = choice_value[my_choice] + fight_value[result] # get round score
    score += round_score # add to score

print(score)