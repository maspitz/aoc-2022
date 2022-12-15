"""Solves day 07, Advent of Code 2022."""

from aocd.models import Puzzle
from typing import Dict, Union
from dataclasses import dataclass

@dataclass
class File:
    """Class to represent a file in the filesystem"""

    name: str
    size: int

    @property
    def total_size(self):
        """Returns the file's size."""
        return self.size


@dataclass
class Directory:
    """Class to represent a directory in the filesystem"""

    name: str
    parent: "Directory"
    contents: Dict[str, Union["Directory", File]]

    @property
    def total_size(self):
        """Returns the total size of all contained files and subdirectories.

        If cyclic subdirectories are present, it will try to recur infinitely,
        and eventually exceed stack space."""

        return sum([x.total_size for x in self.contents.values()])

    def mkdir(self, name: str):
        """Creates a subdirectory having the given name.

        If such a file or subdirectory already exists, there is no effect."""
        if name not in self.contents:
            self.contents[name] = Directory(name, self, dict())

    def create_file(self, name: str, size: int):
        """Creates a file having the given name and size.

        If such a file or subdirectory already exists, there is no effect."""
        if name not in self.contents:
            self.contents[name] = File(name, size)

    def __str__(self) -> str:
        """Returns a brief string representation of the Directory."""
        return f"Directory {self.name}: {[x for x in self.contents.keys()]}"


def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    return "Solution not implemented"


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=7)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
