def read_input(file_path):
    # read the file and return the grid as a list of lists
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


def print_grid(grid):
    for line in grid:
        print("".join(line))


def execute_turn(grid, line):
    splitted = 0
    if line == 0:
        # find the S in the first row
        idx = grid[0].index("S")
        # in the next line, replace the character at the S index with |
        grid[1][idx] = "|"
    else:
        # in the line find all the | characters
        indices = [i for i, char in enumerate(grid[line]) if char == "|"]
        for idx in indices:
            # check what is in the next line at the same index
            below_char = grid[line + 1][idx]
            if below_char == ".":
                grid[line + 1][idx] = "|"
            elif below_char == "^":
                splitted += 1
                # we split the flow to the left and right
                if idx > 0:
                    grid[line + 1][idx - 1] = "|"
                if idx < len(grid[line + 1]) - 1:
                    grid[line + 1][idx + 1] = "|"
    return grid, splitted


def compute_result_part1(grid):
    grid_copy = [row[:] for row in grid]
    total_splitted = 0
    for line_num in range(len(grid_copy) - 1):
        grid_copy, splitted = execute_turn(grid_copy, line_num)
        total_splitted += splitted
    return total_splitted


def execute_turn_with_timelines(grid, timeline, line):
    # process one turn and track how many timelines pass through each column
    if line == 0:
        # find the S in the first row and start with 1 timeline
        idx = grid[0].index("S")
        grid[1][idx] = "|"
        timeline[idx] = 1
    else:
        # in the line find all the | characters
        indices = [i for i, char in enumerate(grid[line]) if char == "|"]
        for idx in indices:
            current_timelines = timeline[idx]
            below_char = grid[line + 1][idx]
            if below_char == ".":
                # beam continues down, timeline count stays at same column
                grid[line + 1][idx] = "|"
            elif below_char == "^":
                # beam splits - both paths inherit all timelines
                if idx > 0:
                    grid[line + 1][idx - 1] = "|"
                    timeline[idx - 1] += current_timelines
                if idx < len(grid[line + 1]) - 1:
                    grid[line + 1][idx + 1] = "|"
                    timeline[idx + 1] += current_timelines
                # beam stopped at splitter, no more timelines at this column
                timeline[idx] = 0
    return grid, timeline


def compute_result_part2(grid):
    grid_copy = [row[:] for row in grid]
    timeline = [0] * len(grid_copy[0])
    for line_num in range(len(grid_copy) - 1):
        grid_copy, timeline = execute_turn_with_timelines(grid_copy, timeline, line_num)
    return sum(timeline)


if __name__ == "__main__":
    grid = read_input("2025/inputs/7.txt")
    result_part1 = compute_result_part1(grid)
    print("Part 1:", result_part1)
    result_part2 = compute_result_part2(grid)
    print("Part 2:", result_part2)
