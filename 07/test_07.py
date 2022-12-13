"""Tests for day 07 of Advent of Code 2022."""

import day07

# Test data given as a multiline string.
sample_input_data = "$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

sample_solution_a = 95437

sample_solution_b = "Sample solution not entered"


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day07.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day07.part_b(sample_input_data) == sample_solution_b
