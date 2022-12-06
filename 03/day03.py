"""Solves day 03, Advent of Code 2022."""

from aocd.models import Puzzle


def common_elements(s1: str, s2: str) -> set:
    """Given two input strings, return a set of the elements common to both."""

    return set(s1).intersection(set(s2))


def compartments(rucksack: str) -> tuple:
    """Given a rucksack, returns its two compartments as a tuple."""

    n = len(rucksack)
    if n % 2 != 0:
        raise ValueError("Rucksack can't be divided into two equal parts.")
    return rucksack[:n//2], rucksack[n//2:]


def item_priority(item: str) -> int:
    """Returns an item types' numerical priority."""

    if ord('a') <= ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1

    if ord('A') <= ord(item) <= ord('Z'):
        return ord(item) - ord('A') + 27

    raise ValueError(f"Invalid item type: {item}")


def rucksack_error_priority(rucksack: str):
    """Returns the priority of the misplaced item type in a rucksack."""

    misplaced_items = common_elements(*compartments(rucksack))
    if len(misplaced_items) == 0:
        raise ValueError("Rucksack has no misplaced items.")
    if len(misplaced_items) > 1:
        raise ValueError("Rucksack has more than one misplaced item.")
    return sum(item_priority(item) for item in misplaced_items)


def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    return sum(rucksack_error_priority(rucksack)
               for rucksack in input_data.split('\n'))


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=3)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
