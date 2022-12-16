"""Tests for day 09 of Advent of Code 2022."""

import day09

# Test data given as a multiline string.
sample_input_data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

sample_solution_a = 13

sample_solution_b = "Sample solution not entered"


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day09.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day09.part_b(sample_input_data) == sample_solution_b
