GUARD = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}

def read_input(file_path):
    with open(file_path) as f:
        data = f.read().strip()
    new_data = []
    for line in data.split("\n"):
        new_data.append([elem for elem in line])
    return new_data

def find_guard(data):
    for y, line in enumerate(data):
        for x, elem in enumerate(line):
            if elem in GUARD:
                return (x, y), elem
            
def get_new_guard_position(pos, direction):
    return pos[0] + direction[0], pos[1] + direction[1]

def rotate_clockwise(current_guard):
    if current_guard == "^":
        return ">"
    if current_guard == ">":
        return "v"
    if current_guard == "v":
        return "<"
    if current_guard == "<":
        return "^"

def is_valid(pos, data):
    # check if it is in the grid
    if pos[1] < 0 or pos[1] >= len(data):
        # The guard is out of the grid, we can stop the simulation
        return False, True
    if pos[0] < 0 or pos[0] >= len(data[0]):
        return False, True
    # check if it is a wall
    if data[pos[1]][pos[0]] == "#":
        return False, False
    return True, False

def mark_position(pos, data, char):
    data[pos[1]][pos[0]] = char

def search(start_x, start_y, delta_x, delta_y):
    visited_positions = set()
    while True:
        if (start_x, start_y, delta_x, delta_y) in visited_positions:
            return 1
        visited_positions.add((start_x, start_y, delta_x, delta_y))
        if not (-1 < start_x + delta_x < n and -1 < start_y + delta_y < m):
            return 0
        elif data[start_x + delta_x][start_y + delta_y] == "#":
            delta_x, delta_y = delta_y, -delta_x
            continue
        start_x, start_y = start_x + delta_x, start_y + delta_y

if __name__ == "__main__":
    file_path = "inputs/input6.txt"
    data = read_input(file_path)
    guard = find_guard(data)
    x_positions = [guard[0]]
    stop = False
    while not stop:
        new_pos = get_new_guard_position(guard[0], GUARD[guard[1]])
        valid, stop = is_valid(new_pos, data)
        if valid:
            # mark current position
            mark_position(guard[0], data, "X")
            guard = new_pos, guard[1]
            # mark new position
            mark_position(guard[0], data, guard[1])
        else:
            guard = guard[0], rotate_clockwise(guard[1])
    for i, line in enumerate(data):
        if "X" in line:
            # append all the x positions
            x_positions.extend((i, x) for x, elem in enumerate(line) if elem == "X")
    print(len(x_positions))
    
    # Part 2
    data = read_input(file_path)
    n, m = len(data), len(data[0])
    for row in range(n):
        for col in range(m):
            if data[row][col] == "^":
                start_x, start_y = row, col
                break
    total_searches = 0
    for row in range(n):
        for col in range(m):
            if data[row][col] != "#":
                data[row][col] = "#"
                total_searches += search(start_x, start_y, -1, 0)
                data[row][col] = "."
    print(total_searches)