"""Tests for day 03 of Advent of Code 2022."""

import day03

# Test data given as a multiline string.
sample_input_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

sample_solution_a = 157

sample_solution_b = "Sample solution not entered"


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day03.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day03.part_b(sample_input_data) == sample_solution_b
