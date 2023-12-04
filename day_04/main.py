""" Advent of Code - day 4"""
from typing import List, Optional
from dataclasses import dataclass
from utils.io import load_txt


@dataclass
class Scratchcard:
    """Scratchcard dataclass"""
    card_id: Optional[int]
    winning_numbers: List[int]
    numbers_you_have: List[int]
    matching_numbers: int
    points: int


def preprocess_str_numbers(str_numbers: str, sep: str = " ") -> List[int]:
    """
    Processes a string of numbers and returns a list of integers
    """
    return [int(number.strip())
            for number in str_numbers.split(sep)
            if number]

def get_scratchcard(string_value: str) -> Scratchcard:
    """
    Processes the string_value and returns a Scratchcard instance
    """
    str_card_id, numbers = string_value.split(':')
    card_id = int(str_card_id.replace('Card','').strip())

    str_winning_numbers, str_numbers_you_have = numbers.split('|')
    winning_numbers=preprocess_str_numbers(str_winning_numbers)
    numbers_you_have=preprocess_str_numbers(str_numbers_you_have)
    matching_numbers = retrieve_matching_numbers(winning_numbers, numbers_you_have)

    return Scratchcard(
        card_id=card_id,
        winning_numbers=winning_numbers,
        numbers_you_have=numbers_you_have,
        matching_numbers=matching_numbers,
        points=2**(matching_numbers - 1) if matching_numbers else 0
    )

def retrieve_matching_numbers(winning_numbers: List[int],
                              numbers_you_have: List[int]) -> int:
    """
    Retrives number of matching numbers between winning numbers and numbers_you_have
    """
    num_matches = 0
    for winning_number in winning_numbers:
        if winning_number in numbers_you_have:
            num_matches += 1
    return num_matches


def main():

    puzzle_input = load_txt('resources/puzzle_input.txt')

    # Part one
    scratchcards = [get_scratchcard(row) for row in puzzle_input]
    sum_points = sum(scratchcard.points for scratchcard in scratchcards)
    print(f"Sum of scratchcard points: {sum_points}")

    # Part two
    for s in scratchcards:
        scratchcards.extend(scratchcards[s.card_id: s.card_id + s.matching_numbers])
    print(f"Total scratchcards: {len(scratchcards)}")

if __name__ == "__main__":
    main()
