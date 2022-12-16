"""Solves day 09, Advent of Code 2022."""

from aocd.models import Puzzle
from collections import namedtuple
from dataclasses import dataclass

Point = namedtuple("Point", "x y")


def add_points(a: Point, b: Point) -> Point:
    """Returns the sum of two points."""
    return Point(a.x + b.x, a.y + b.y)


def sub_points(a: Point, b: Point) -> Point:
    """Returns the difference of two points (a - b)."""
    return Point(a.x - b.x, a.y - b.y)


DIRECTION = {"U": Point(0, 1),
             "L": Point(-1, 0),
             "R": Point(1, 0),
             "D": Point(0, -1)}


def sign(n: int) -> int:
    """Returns -1, 0, or 1 to indicate the sign of an integer."""
    return (n > 0) - (n < 0)


@dataclass
class Bridge:
    """Models the bridge configuration."""

    head: Point = Point(0, 0)
    tail: Point = Point(0, 0)

    def move_tail(self):
        """Moves the tail according to the head's position."""

        offset = sub_points(self.head, self.tail)

        if abs(offset.x) >= 2 or abs(offset.y) >= 2:
            self.tail = add_points(self.tail,
                                   Point(sign(offset.x), sign(offset.y)))


def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    b = Bridge()
    tail_history = set()

    for line in input_data.split('\n'):
        heading, amount = line.split(' ')
        for _ in range(int(amount)):
            b.head = add_points(b.head, DIRECTION[heading])
            b.move_tail()
            tail_history.add(b.tail)

    return len(tail_history)


def part_b(input_data: str) -> str:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=9)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
