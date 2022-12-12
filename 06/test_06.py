"""Tests for day 06 of Advent of Code 2022."""

import day06

# Test data given as a multiline string.
sample_input_data = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
                     "bvwbjplbgvbhsrlpgdmjqwftvncz",
                     "nppdvjthqldpwncqszvftbrmjlhg",
                     "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
                     "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]

sample_solution_a = [7, 5, 6, 10, 11]

sample_solution_b = [19, 23, 23, 29, 26]


def test_part_a():
    """Test the solution on sample data for part A."""
    for data, soln in zip(sample_input_data, sample_solution_a):
        assert day06.part_a(data) == soln


def test_part_b():
    """Test the solution on sample data for part B."""
    for data, soln in zip(sample_input_data, sample_solution_b):
        assert day06.part_b(data) == soln
