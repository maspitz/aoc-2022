"""Solves day 02, Advent of Code 2022."""

from aocd.models import Puzzle

ROCK = 1
PAPER = 2
SCISSORS = 3

SHAPE_CODE = {"A": ROCK,
              "B": PAPER,
              "C": SCISSORS,
              "X": ROCK,
              "Y": PAPER,
              "Z": SCISSORS}

DEFEATER_OF = {ROCK: PAPER,
               PAPER: SCISSORS,
               SCISSORS: ROCK}


def round_score_a(input_line: str) -> int:
    """Calculate the score for one round in part a."""

    opponent_shape = SHAPE_CODE[input_line[0]]
    player_shape = SHAPE_CODE[input_line[2]]

    score = player_shape
    if DEFEATER_OF[opponent_shape] == player_shape:
        score += 6
    elif DEFEATER_OF[player_shape] == opponent_shape:
        pass
    else:
        score += 3

    return score
    

def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    return sum(round_score_a(line) for line in input_data.split("\n"))


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=2)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
