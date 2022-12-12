"""Solves day 06, Advent of Code 2022."""

from aocd.models import Puzzle

from collections import deque

def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    if len(input_data) < 4:
        raise ValueError("Input data is less than four characters long.")

    marker = deque(input_data[:3])
    marker_pos = 3
    for ch in input_data[3:]:
        marker.append(ch)
        marker_pos += 1
        if len(set(marker)) == 4:
            return marker_pos
        else:
            marker.popleft()
    raise ValueError("Input data has no sequence of four consecutive "
                     "unique characters.")
    return None


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=6)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
