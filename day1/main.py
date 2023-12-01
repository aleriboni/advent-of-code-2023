""" Advent of Code - day 1"""
import re
from typing import List, Optional, Dict
from utils.io import load_txt


def merge_first_last_digits_in_list(digit_list: List[str]) -> Optional[int]:
    """
    Merges the first and last digits in a string and converts it in an integer.
    """
    if digit_list:
        return int("".join(digit_list[0] + digit_list[-1]))
    print("No digits in the input string")
    return None

def get_calibration_value_part_one(string_value: str) -> Optional[int]:
    """
    Retrieves the calibration value for the input string_value for part one
    """
    digit_list = [character for character in string_value if character.isdigit()]
    return merge_first_last_digits_in_list(digit_list)

def get_calibration_value_part_two(string_value: str, digits_in_word: Dict) -> Optional[int]:
    """
    Retrieves the calibration value for the input string_value for part two
    """
    all_digits = list(digits_in_word.keys()) + list(digits_in_word.values())
    pattern = "(?=(" + "|".join(all_digits) + "))"
    matches = re.findall(pattern=pattern, string=string_value)
    digit_list = [digits_in_word[match] if digits_in_word.get(match) else match
                  for match in matches]
    return merge_first_last_digits_in_list(digit_list)

def main():

    # Load puzzle input
    puzzle_input = load_txt('resources/puzzle_input.txt')

    # Part 1
    result_puzzle_input_1 = [get_calibration_value_part_one(row)
                           for row in puzzle_input]
    print(f"Sum of calibration values for part 1: {sum(result_puzzle_input_1)}")

    # Part 2
    digits_in_word = {
        'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8', 
        'nine': '9'
    }
    result_puzzle_input_2 = [get_calibration_value_part_two(row, digits_in_word)
                             for row in puzzle_input]
    print(f"Sum of calibration values for part 2: {sum(result_puzzle_input_2)}")


if __name__ == "__main__":
    main()
