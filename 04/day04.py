"""Solves day 04, Advent of Code 2022."""

from aocd.models import Puzzle

from parse import parse

def parse_assignment_pair(line: str) -> tuple:
    """Parses an input line, returning a pair of assigned ranges.

    Ranges are in the form (lo, hi), where lo <= hi.

    Example:
           parse_assignment_pair("1-4,2-6")
    Returns:
           ((1, 4), (2, 6))"""

    p = parse("{:d}-{:d},{:d}-{:d}", line)
    if p == None:
        raise(f"Could not parse line: {line}")
    a_lo, a_hi, b_lo, b_hi = p.fixed
    if a_lo > a_hi or b_lo > b_hi:
        raise(f"Incorrect ordering of range in line: {line}")
    return ((a_lo, a_hi), (b_lo, b_hi))

def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    assignments = [parse_assignment_pair(line)
                   for line in input_data.split('\n')]

    fully_contained = sum((a_lo <= b_lo and b_hi <= a_hi) or
                          (b_lo <= a_lo and a_hi <= b_hi)
                          for ((a_lo, a_hi), (b_lo, b_hi)) in assignments)

    return fully_contained



def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=4)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
