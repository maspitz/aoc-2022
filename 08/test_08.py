"""Tests for day 08 of Advent of Code 2022."""

import day08

# Test data given as a multiline string.
sample_input_data = """30373
25512
65332
33549
35390"""

sample_solution_a = 21

sample_solution_b = "Sample solution not entered"


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day08.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day08.part_b(sample_input_data) == sample_solution_b
