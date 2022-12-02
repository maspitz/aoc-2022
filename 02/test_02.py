"""Tests for day 02 of Advent of Code 2022."""

import day02

# Test data given as a multiline string.
sample_input_data = """A Y
B X
C Z"""

sample_solution_a = 15

sample_solution_b = "Sample solution not entered"


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day02.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day02.part_b(sample_input_data) == sample_solution_b
