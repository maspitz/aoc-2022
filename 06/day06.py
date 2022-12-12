"""Solves day 06, Advent of Code 2022."""

from aocd.models import Puzzle

from collections import deque


def find_marker(input_data: str, marker_len: int) -> int:
    """Returns a marker index for the input_data.

    To be more specific, the 'marker index' is the index
    of the character that immediately follows the marker, where
    the marker is defined as the first substring of input_data
    which consists of marker_len distinct characters."""

    if len(input_data) < marker_len:
        raise ValueError(f"Input data is less than {marker_len} characters long.")

    marker = deque(input_data[:marker_len-1])
    marker_pos = marker_len-1
    for ch in input_data[marker_len-1:]:
        marker.append(ch)
        marker_pos += 1
        if len(set(marker)) == marker_len:
            return marker_pos
        else:
            marker.popleft()
    raise ValueError(f"Input data has no sequence of {marker_len} consecutive "
                     "unique characters.")
    return None


def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    return find_marker(input_data, 4)

def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return find_marker(input_data, 14)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=6)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
