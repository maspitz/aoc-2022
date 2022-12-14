"""Solves day 07, Advent of Code 2022."""

from aocd.models import Puzzle

# We will infer the filesystem contents from the command history.
# Directories will be modeled as dicts using string as keys.
# The root directory has an entry with key ".." containing value None.
# For all subdirectories, the ".." entry contains its parent directory.
# Files are entries whose values are file sizes (assumed to be ints).

# We assume that the command history is consistent throughout: that is,
# directory contents will not change on different executions of 'ls',
# a single 'ls' will not reveal multiple files of the same name, etc.
# We also assume file and directory names contain no spaces
# (though this requirement would be easy to relax if needed).

def add_entry(subdir: dict, entry_line: str):
    """Adds an entry to a subdirectory based on a line from the output of ls.

    For example:
      add_entry(subdir, "173 foo.txt") adds a file 'foo.txt' of size 173.
      add_entry(subdir, "dir bar") adds a subdirectory named 'bar'."""

    stat, name = entry_line.split(' ')
    if stat == "dir":
        if name not in subdir:
            subdir[name] = {"..": subdir}
    else:
        size = int(stat)
        subdir[name] = size

def process_commands(commands: list) -> dict:
    """Processes the commands in the command history, returning the root directory.

    Each commands includes the command line as well as any output."""

    rootdir = {"..": None}
    current_dir = rootdir

    for command_history in commands:
        lines = command_history.split('\n')
        argv = lines[0].split(' ')
        command_output = lines[1:]
        command = argv[0]
        if command == 'ls':
            for entry in command_output:
                add_entry(current_dir, entry)
        elif command == 'cd':
            argument = argv[1]
            if argument == '/':
                current_dir = rootdir
            else:
                if '/' in argument:
                    raise ValueError("Path specification containing slash not implemented.")
                if argument not in current_dir:
                    add_entry(current_dir, "dir "+argument)
                    print("Warning: cd to previously unseen directory.")
                current_dir = current_dir[argument]
                if current_dir == None:
                    raise ValueError("Can't cd to parent of root directory.")
    return rootdir


def subdir_sizes(directory: dict) -> dict:
    """Returns a flat list containing the total sizes of the directory and its subdirectories."""

    dir_sizes = []
    dir_size = 0
    for name, val in directory.items():
        if name == '..':
            continue
        if isinstance(val, int):
            dir_size += val
        elif isinstance(val, dict):
            sub_sizes = subdir_sizes(val)
            dir_sizes.extend(sub_sizes)
            dir_size += max(sub_sizes)
    dir_sizes.append(dir_size)
    return dir_sizes


def split_history(input_data: str) -> str:
    """Splits the command history into multiline entries based on the command prompt '\n$ '"""

    commands = input_data.split('\n$ ')
    if commands[0][0:2] == '$ ':
        commands[0] = commands[0][2:]
    return commands


def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    rootdir = process_commands(split_history(input_data))
    sizes = subdir_sizes(rootdir)
    return sum(size for size in sizes if size <= 100000)


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    rootdir = process_commands(split_history(input_data))
    sizes = subdir_sizes(rootdir)
    TOTAL_SPACE = 70000000
    UPDATE_SIZE = 30000000
    used_space = max(sizes)
    unused_space = TOTAL_SPACE - used_space
    additional_space_needed = UPDATE_SIZE - unused_space

    return min(size for size in sizes if size >= additional_space_needed)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=7)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
