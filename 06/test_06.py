"""Tests for day 06 of Advent of Code 2022."""

import day06

# Test data given as a multiline string.
sample_input_data = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
                     "bvwbjplbgvbhsrlpgdmjqwftvncz",
                     "nppdvjthqldpwncqszvftbrmjlhg",
                     "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
                     "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]

sample_solution_a = [7, 5, 6, 10, 11]

sample_solution_b = "Sample solution not entered"


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day06.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day06.part_b(sample_input_data) == sample_solution_b
