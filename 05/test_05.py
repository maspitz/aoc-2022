"""Tests for day 05 of Advent of Code 2022."""

import day05

# Test data given as a multiline string.
sample_input_data = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

sample_solution_a = "CMZ"

sample_solution_b = "MCD"


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day05.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day05.part_b(sample_input_data) == sample_solution_b
