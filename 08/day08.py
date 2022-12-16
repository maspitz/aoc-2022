"""Solves day 08, Advent of Code 2022."""

from aocd.models import Puzzle
import numpy as np


def parse_data(input_data: str) -> np.array:
    """Parse the single digit tree data into an np.array"""
    digits = [[int(digit) for digit in line]
              for line in input_data.split()]
    return np.array(digits, dtype=int)


def tree_visibility_from_top(tree_heights: np.array) -> np.array:
    """Returns a np.array of bools showing which trees are visible from the top."""

    rows, cols = tree_heights.shape

    # running height of trees visible from the top, oriented as a row left to right,
    # initialized to -1 so that all trees along the top row will be marked visible
    running_visible_height = -1 * np.ones((1, cols), dtype=int)

    tree_visibility = np.zeros_like(tree_heights, dtype=bool)

    for row in range(rows):
        tree_visibility[row,:] = tree_heights[row,:] > running_visible_height
        running_visible_height = np.maximum(tree_heights[row,:], running_visible_height)

    return tree_visibility

    
def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    tree_heights = parse_data(input_data)

    vis_top = tree_visibility_from_top(tree_heights)
    vis_left = tree_visibility_from_top(tree_heights.transpose()).transpose()
    vis_bottom = np.flip(tree_visibility_from_top(np.flip(tree_heights)))
    vis_right = np.flip(tree_visibility_from_top(np.flip(tree_heights).transpose()).transpose())
    visible_trees = np.logical_or(np.logical_or(vis_top, vis_left),
                                  np.logical_or(vis_bottom, vis_right))

    return np.sum(visible_trees)


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=8)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
