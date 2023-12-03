""" Advent of Code - day 3"""
import re
from typing import List
from utils.io import load_txt

SPECIAL_CHARACTERS = '*%#/$=@+&-'

def retrieve_row_part_numbers(rows: List[str]) -> List[int]:

    min_size = 0
    max_size = len(rows[0])
    part_numbers = []
    candidates_numbers = re.finditer(r'\d+', rows[1])
    for match in candidates_numbers:
        span = match.span()
        adjust_span = (max(span[0] - 1, min_size), min(span[1] + 1, max_size))
        string_to_check = "".join(row[adjust_span[0]: adjust_span[1]]
                                  for row in rows)
        if any(c in SPECIAL_CHARACTERS for c in string_to_check):
            part_numbers.append(int(match.group(0)))
    return part_numbers

def retrieve_gear_ratios(rows: List[str]) -> List[int]:

    gear_ratios = []
    min_size = 0
    max_size = len(rows[0])
    candidates_gear = re.finditer(r'\*', rows[1])
    for match_gear in candidates_gear:
        gear_found = []
        gear_position = match_gear.start()

        for row in rows:
            candidates_numbers = re.finditer(r'\d+', row)
            for match_number in candidates_numbers:
                if gear_position >= match_number.start() - 1 and gear_position <= match_number.end():
                    gear_found.append(int(match_number.group(0)))
        if len(gear_found) == 2:
            gear_ratios.append(gear_found[0] * gear_found[1])
    return gear_ratios
def main():

    puzzle_input = load_txt('resources/puzzle_input.txt')
    
    # Part one
    # add first and last line
    dummy_line = ['.' * len(puzzle_input[0])]
    puzzle_input = dummy_line + puzzle_input + dummy_line

    part_numbers = [retrieve_row_part_numbers(puzzle_input[i:i+3])
                    for i in range(0, len(puzzle_input) - 2)]

    sum_part_numbers = sum([sum(row_numbers) for row_numbers in part_numbers])
    print(f"Sum of part numbers: {sum_part_numbers}")

    # Part two
    gear_ratios = [retrieve_gear_ratios(puzzle_input[i:i+3])
                   for i in range(0, len(puzzle_input) - 2)]
    
    sum_gear_ratios = sum([sum(row_gear_ratios) for row_gear_ratios in gear_ratios])
    print(f"Sum of gear ratios: {sum_gear_ratios}")
if __name__ == "__main__":
    main()
