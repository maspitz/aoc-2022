"""Solves day 01, Advent of Code 2022."""

from aocd.models import Puzzle


def calorie_totals(input_data: str) -> list:
    """Given puzzle input data, return a list of of each elf's total calories."""

    elves_food = input_data.split("\n\n")
    calorie_totals = [sum(int(calories) for calories in elf_food.split("\n"))
                          for elf_food in elves_food]
    return calorie_totals


def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    return max(calorie_totals(input_data))


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    cal_totals = calorie_totals(input_data)

    top_three_totals = sorted(cal_totals)[-3:]

    return sum(top_three_totals)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=1)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
