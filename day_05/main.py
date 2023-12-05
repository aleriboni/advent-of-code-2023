""" Advent of Code - day 5"""
from typing import List, Optional
from dataclasses import dataclass
from utils.io import load_txt
from dataclasses import dataclass

@dataclass
class Line:
    dest_range_start: int
    source_range_start: int
    range_length: int

@dataclass
class Map:
    source_category: str
    dest_category: str
    lines: List[Line]

@dataclass
class Almanac:
    seeds: List[int]
    maps: List[Map]

def retrieve_seeds_for_part_two(seeds: List[int]) -> List[int]:

    seeds_part_two = []
    for idx, seed in enumerate(seeds):
        if idx % 2 == 0:
            seeds_part_two.extend(list(range(seed, seed + seeds[idx + 1])))
    return seeds_part_two

def convert_string_in_numbers(str_numbers: str, sep: str = " ") -> List[int]:
    
    return [int(item.strip()) for item in str_numbers.split(sep) if item]

def process_map_header(string_value: str) -> (str, str):

    return string_value.replace(' map:', '').split('-to-')


def process_map_line(str_line: str) -> Line:
    
    line = convert_string_in_numbers(str_line)
    return Line(dest_range_start=line[0],
                source_range_start=line[1],
                range_length=line[2])

def process_map_lines(str_lines: List[str]) -> List[Line]:

    return [process_map_line(str_line) for str_line in str_lines if str_line]


def create_map(map_lines: List[str]) -> Map:

    source, dest = process_map_header(map_lines[0])
    lines = process_map_lines(map_lines[1:])

    return Map(
        source_category=source,
        dest_category=dest,
        lines=lines
    )
def process_puzzle_input(puzzle_input: List[str], part: str = 'one') -> Almanac:

    list_maps = []
    seeds_str = puzzle_input[0].split(':')[1]
    seeds = convert_string_in_numbers(seeds_str)
    if part == 'two':
        seeds = retrieve_seeds_for_part_two(seeds)

    map_indexes = [puzzle_input.index(row) for row in puzzle_input[1:] 
                   if 'map' in row or puzzle_input.index(row) == len(puzzle_input) - 1]

    for index, map_index in enumerate(map_indexes):
        if map_index < len(puzzle_input) - 1:
            list_maps.append(create_map(map_lines=puzzle_input[map_index:map_indexes[index + 1]]))
        
    return Almanac(
        seeds=seeds,
        maps=list_maps
    )

def retrieve_location_numbers(almanac: Almanac):

    location_numbers = []
    for seed in almanac.seeds:
        number = seed
        for puzzle_map in almanac.maps:
            next_number = number
            for line in puzzle_map.lines:
                diff = number - line.source_range_start
                if diff < line.range_length and diff >= 0:
                    next_number = line.dest_range_start + diff
            number = next_number
        location_numbers.append(number)
    return location_numbers

def main():

    puzzle_input = load_txt('resources/puzzle_input.txt')
    almanac_one = process_puzzle_input(puzzle_input, part='one')

    # Part one
    location_numbers_one = retrieve_location_numbers(almanac=almanac_one)
    
    for seed, location_number in zip(almanac_one.seeds, location_numbers_one):
        print(f"Seed: {seed} -> location number: {location_number}")
    print(f"Lowest location number: {min(location_numbers_one)}")


if __name__ == "__main__":
    main()
