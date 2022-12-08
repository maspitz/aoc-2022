"""Tests for day 04 of Advent of Code 2022."""

import day04

# Test data given as a multiline string.
sample_input_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

sample_solution_a = 2

sample_solution_b = 4


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day04.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day04.part_b(sample_input_data) == sample_solution_b
