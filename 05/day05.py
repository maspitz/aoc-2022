"""Solves day 05, Advent of Code 2022."""

from aocd.models import Puzzle
from parse import parse
from typing import List
from collections import namedtuple
import re

CrateMove = namedtuple("CrateMove", "n, src, dst")
# n: How many crates to move
# src: Source stack #
# dst: Destination stack #

def parse_stacks(stacks_data: str) -> list[list[str]]:
    """Returns the state of the stacks.

    The full state is a list of stack states.
    Each stack state is a list of crate names."""

    lines = stacks_data.split('\n')

    stack_names_re = re.compile('[0-9]+')
    names = stack_names_re.findall(lines[-1])
    if len(names) > 9:
        raise ValueError("Got too many stacks ({len(names)})")
    for idx, name_str in enumerate(names):
        if str(idx+1) != name_str:
            raise ValueError("Did not find expected numerical stack sequence.")

    crate_pattern = re.compile('[\[ ]([ A-Z0-9])[\] ] ?')

    stacks = [[] for _ in names]

    for line in reversed(lines[:-1]):
        line_contents = crate_pattern.findall(line)
        for stack_idx, crate in enumerate(line_contents):
            if crate != ' ':
                stacks[stack_idx].append(crate)

    return stacks


def move_crates(stacks: list[list[str]], moves: list[str]) -> None:
    """Modifies the stacks list by applying the specified crate moves."""

    for move in moves:
        parsed_move = parse('move {:d} from {:d} to {:d}', move)
        if parsed_move == None:
            raise ValueError("Could not parse move: {move}")

        # Note: in the move specifications, stacks are indexed starting at 1
        num_crates, src, dst = parsed_move
        for _ in range(num_crates):
            crate = stacks[src-1].pop()
            stacks[dst-1].append(crate)

    return None


def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    stack_data, move_data = input_data.split('\n\n')
    stacks = parse_stacks(stack_data)
    moves = move_data.split('\n')

    move_crates(stacks, moves)

    # Note: If any stack is empty at this point, this will raise an IndexError
    stack_tops = [stack[-1] for stack in stacks]

    return "".join(stack_tops)


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=5)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
