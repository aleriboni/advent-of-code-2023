""" Advent of Code - day 2"""
import re
from typing import List
from dataclasses import dataclass
from utils.io import load_txt


@dataclass
class Game:
    """Game dataclass"""
    id: int
    max_green: int = 0
    max_blue: int = 0
    max_red: int = 0


def get_cubes_per_color(list_of_subsets: List[str], color: str) -> int:
    """
    Retrieves the maximum cubes grabed in the list of subset for the input color
    """
    max_grabs = 0
    for subset in list_of_subsets:
        match = re.search(rf'(\d+) {color}', subset)
        if match:
            if int(match.group(1)) > max_grabs:
                max_grabs = int(match.group(1))
    return max_grabs

def process_row_game(string_value: str) -> Game:
    """
    Processes a string row and returns a Game instance
    """
    game, subsets_of_cubes = string_value.split(":")
    list_of_subsets = subsets_of_cubes.split(';')
    return Game(id=int(game.replace('Game ', '').strip()),
                max_green=get_cubes_per_color(list_of_subsets, 'green'),
                max_blue=get_cubes_per_color(list_of_subsets, 'blue'),
                max_red=get_cubes_per_color(list_of_subsets, 'red'))

def main():

    puzzle_input = load_txt('resources/puzzle_input.txt')
    games = [process_row_game(row )for row in puzzle_input]

    # Part one
    possible_games = [game for game in games
                      if game.max_blue <= 14 and game.max_green <= 13
                      and game.max_red <= 12]
    sum_ids = sum(game.id for game in possible_games)
    print(f"Number of possible games: {len(possible_games)}")
    print(f"ID sum of possible games: {sum_ids}")

    # Part two
    power_minimum_set = [game.max_blue * game.max_green * game.max_red 
                         for game in games]
    print(f"Sum of the power of minimum set: {sum(power_minimum_set)}")

if __name__ == "__main__":
    main()
