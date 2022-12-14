"""Solves day 03, Advent of Code 2022."""

from aocd.models import Puzzle


def common_elements(str_list: list) -> set:
    """Given a list of input strings, return a set of their common elements."""
    return set.intersection(*[set(item) for item in str_list])


def compartments(rucksack: str) -> tuple:
    """Given a rucksack, returns its two compartments as a list."""

    n = len(rucksack)
    if n % 2 != 0:
        raise ValueError("Rucksack can't be divided into two equal parts.")
    return [rucksack[:n//2], rucksack[n//2:]]


def item_priority(item: str) -> int:
    """Returns an item types' numerical priority."""

    if ord('a') <= ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1

    if ord('A') <= ord(item) <= ord('Z'):
        return ord(item) - ord('A') + 27

    raise ValueError(f"Invalid item type: {item}")


def rucksack_error_priority(rucksack: str):
    """Returns the priority of the misplaced item type in a rucksack."""

    misplaced_items = common_elements(compartments(rucksack))
    if len(misplaced_items) == 0:
        raise ValueError("Rucksack has no misplaced items.")
    if len(misplaced_items) > 1:
        raise ValueError("Rucksack has more than one misplaced item.")
    (item,) = misplaced_items
    return item_priority(item)


def partition_by_n(full: list, n: int) -> list:
    """Returns the input partitioned into sublists of length n.

    The input length is required to be divisible by n."""

    if len(full) % n != 0:
        raise ValueError("Input length not divisible by %{n}.")

    return [full[i:i+n] for i in range(0, len(full), n)]


def group_badge(elf_group: list) -> str:
    """Determines the badge of an elf group."""

    common_items = set.intersection(*(set(rucksack) for rucksack in elf_group))

    if len(common_items) == 0:
        raise ValueError("Elf group has no common items")
    if len(common_items) > 1:
        raise ValueError("Elf group has more than one common item")
    (badge,) = common_items
    return badge


def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    return sum(rucksack_error_priority(rucksack)
               for rucksack in input_data.split('\n'))


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    elf_groups = partition_by_n(input_data.split('\n'), 3)

    return sum(item_priority(group_badge(elf_group))
               for elf_group in elf_groups)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=3)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
