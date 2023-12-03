"""Advent of Code 2023 - Challenge 2"""
from functools import reduce
from dataclasses import dataclass, fields

@dataclass
class Round:
    green: int = 0
    blue: int = 0
    red: int = 0

    @classmethod
    def _from_raw(cls, round_: str):
        values = { key: int(value) for value, key in (item.split(" ") for item in round_.split(", ")) }
        return cls(**values)
        
@dataclass
class Game:
    id: int
    rounds: list[Round]

    @classmethod
    def _from_raw(cls, row: str):
        game, rounds = row.split(": ")
        game_id = int(game.split(" ")[-1])
        return cls(game_id, [Round._from_raw(r.strip()) for r in rounds.split(";")])

def get_data(filename) -> list[Game]:
    """ load data from file """
    with open(filename, 'r') as file:
        inputs = [Game._from_raw(row.strip()) for row in file.readlines()]
    return inputs

def is_valid_game(game: Game) -> bool:
    for round in game.rounds:
        if round.blue > 14 or round.red > 12 or round.green > 13:
            return False
    return True

def part_1(games: list[Game]):
    valid_game_ids = [game.id for game in games if is_valid_game(game)]
    return sum(valid_game_ids)

def part_2(games: list[Game]):
    powers = []
    for game in games:
        maxes = [ max(getattr(round, key.name) for round in game.rounds) for key in fields(Round)]
        powers.append(reduce((lambda x,y: x*y), maxes))
    return sum(powers)

if __name__ == "__main__":
    data = get_data("2023/inputs/day2.txt")
    data = get_data("2023/inputs/sample-input.txt")
    print("Part 1", part_1(data))
    print("Part 2", part_2(data))
