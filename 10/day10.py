"""Solves day 10, Advent of Code 2022."""

from aocd.models import Puzzle


def register_history(input_program: str) -> list:
    """Given puzzle input, return the register history as a zero-indexed list.

    The list is indexed by cycle, 0 being the first, so that the input data:
      noop
      addx 3
      addx -5
    will return:
    [1, 1, 1, 4, 4, -1]
    """

    results = []
    register = 1
    for instruction in input_program.split('\n'):
        if instruction == 'noop':
            results.append(register)
        else:
            cmd, arg = instruction.split()
            if cmd != 'addx':
                raise ValueError(f"Unknown instruction: {instruction}")
            results.append(register)
            results.append(register)
            register += int(arg)
    results.append(register)
    return results


def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    reg = register_history(input_data)

    return sum([x * reg[x - 1] for x in [20, 60, 100, 140, 180, 220]])


def render_image(input_program: str) -> str:
    """Render as a string the CRT output produced by the input program."""

    output = ""
    reg_hist = register_history(input_program)
    for cycle, reg in enumerate(reg_hist):
        pixel = cycle % 40
        if reg - 1 <= pixel <= reg + 1:
            output += "#"
        else:
            output += '.'
    num_lines = len(output) // 40
    image = "\n".join([output[i:i+40] for i in range(0, num_lines * 40, 40)])
    return image


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return render_image(input_data)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=10)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
