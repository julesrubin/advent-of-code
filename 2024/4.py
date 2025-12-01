def read_input(file_path):
    with open(file_path) as f:
        data = f.read().strip()

    return data


def get_lines(data):
    # return a list of horizontal lines
    return data.split("\n")


def get_columns(data):
    # return one array for each position in the line
    lines = get_lines(data)
    columns = []
    for i in range(len(lines[0])):
        column = []
        for line in lines:
            column.append(line[i])
        columns.append(str("".join(column)))
    return columns


def get_diagonals(data):
    # Return all diagonals (left-to-right and right-to-left)
    lines = get_lines(data)
    num_rows = len(lines)
    num_cols = len(lines[0])
    diagonals = []

    # Left-to-right diagonals
    for start_col in range(num_cols):
        diagonal = []
        row, col = 0, start_col
        while row < num_rows and col < num_cols:
            diagonal.append(lines[row][col])
            row += 1
            col += 1
        diagonals.append("".join(diagonal))

    for start_row in range(1, num_rows):
        diagonal = []
        row, col = start_row, 0
        while row < num_rows and col < num_cols:
            diagonal.append(lines[row][col])
            row += 1
            col += 1
        diagonals.append("".join(diagonal))

    # Right-to-left diagonals
    for start_col in range(num_cols):
        diagonal = []
        row, col = 0, start_col
        while row < num_rows and col >= 0:
            diagonal.append(lines[row][col])
            row += 1
            col -= 1
        diagonals.append("".join(diagonal))

    for start_row in range(1, num_rows):
        diagonal = []
        row, col = start_row, num_cols - 1
        while row < num_rows and col >= 0:
            diagonal.append(lines[row][col])
            row += 1
            col -= 1
        diagonals.append("".join(diagonal))

    return diagonals


def count_xmas(text):
    # count the number of xmas in the text and the reverse text
    return text.count("XMAS") + text.count("SAMX")


def count_crossed_mas(lines):
    total = 0
    rows, cols = len(lines), len(lines[0])

    for i in range(1, rows - 1):  # Avoid top and bottom edges
        for j in range(1, cols - 1):  # Avoid left and right edges
            if lines[i][j] == "A":
                # Check if the diagonals form an X-MAS pattern
                top_left = lines[i - 1][j - 1]
                top_right = lines[i - 1][j + 1]
                bottom_left = lines[i + 1][j - 1]
                bottom_right = lines[i + 1][j + 1]

                if (top_left + bottom_right in ["MS", "SM"]) and (
                    top_right + bottom_left in ["MS", "SM"]
                ):
                    total += 1

    return total

if __name__ == "__main__":
    file_path = "inputs/input4.txt"
    data = read_input(file_path)
    lines = get_lines(data)
    columns = get_columns(data)
    diagonals = get_diagonals(data)
    print(sum(count_xmas(text) for text in lines + columns + diagonals))
    print(count_crossed_mas(lines))