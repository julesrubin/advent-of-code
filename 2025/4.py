def read_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines

def is_valid(x, y, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] == '@':
                count += 1
                if count > 3:
                    return False
    return True

def compute_result_part1(data):
    grid = [list(line) for line in data]
    rows = len(grid)
    cols = len(grid[0])
    valid_pos = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                if is_valid(i, j, grid):
                    valid_pos.append((i, j))
    return len(valid_pos), valid_pos

def compute_result_part2(data):
    # iterate through the grid, at each turn, remove valid '@' positions
    grid = [list(line) for line in data]
    rows = len(grid)
    cols = len(grid[0])
    removal_count = 0
    while True:
        to_remove = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@':
                    if is_valid(i, j, grid):
                        to_remove.append((i, j))
        if not to_remove:
            break
        for x, y in to_remove:
            grid[x][y] = '.'
            removal_count += 1
    return removal_count

if __name__ == "__main__":
    input_lines = read_input("2025/inputs/4.txt")
    result_part1, _ = compute_result_part1(input_lines)
    print(f"Result Part 1: {result_part1}")
    result_part2 = compute_result_part2(input_lines)
    print(f"Result Part 2: {result_part2}")