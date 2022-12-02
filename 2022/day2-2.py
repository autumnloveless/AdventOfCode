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

choice_comparison = {
    "A": "C", # rock beats sissor
    "B": "A", # paper beats rock
    "C": "B" # sissor beats paper
}

def fight(opponent_choice, my_choice) -> int:
    if opponent_choice == my_choice:
        return 3 # tie
    if choice_comparison[my_choice] == opponent_choice:
        return 6 # I win
    else:
        return 0 # I lose
    

# Determine score
score = 0
for line in input:
    [opponent_choice, my_choice_encrypted] = line.strip().split(" ") # process input
    my_choice = choice_mapping[my_choice_encrypted] # convert to A,B,C
    round_score = fight(opponent_choice, my_choice) + choice_value[my_choice] # get round score
    score += round_score # add to score

print(score)