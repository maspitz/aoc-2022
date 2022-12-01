"""Tests for day 01 of Advent of Code 2022."""

import day01

# Test data given as a multiline string.
sample_input_data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

sample_solution_a = "24000"

sample_solution_b = "Sample solution not entered"


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day01.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day01.part_b(sample_input_data) == sample_solution_b
