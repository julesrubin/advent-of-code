def read_input(file_path):
    with open(file_path, "r") as file:
        return [line.strip().split() for line in file.readlines()]

def transform_data(lines):
    # from lines, we want to get columns
    transposed = []
    for col_idx in range(len(lines[0])):
        column = [row[col_idx] for row in lines]
        transposed.append(column)
    return transposed

def compute_result_part1(columns):
    total = 0
    for col in columns:
        # compute value for this column
        if col[-1] == '+':
            total += sum(int(x) for x in col[:-1])
        elif col[-1] == '*':
            prod = 1
            for x in col[:-1]:
                prod *= int(x)
            total += prod
    return total

def read_input_part2(file_path):
    # return columns without stripping spaces
    with open(file_path, "r") as file:
        lines = file.readlines()
    return [line.rstrip('\n') for line in lines]

def compute_result_part2(columns):
    # Cephalopod math is written right-to-left in columns. Cephalopod have very weird math rules ¯\_(ツ)_/¯
    total = 0
    operator = None
    to_compute = []
    for char_idx in range(len(columns[0]) - 1, -1, -1):
        number = "".join(line[char_idx] for line in columns).strip()
        print(number)
        # if number is only constituted of spaces, skip
        if not number or all(c == ' ' for c in number):
            continue
        if number[-1] in ['+', '*'] and len(number.strip()) > 1:
            operator = number[-1]
            number = number[:-1]
        to_compute.append(int(number))
        print(to_compute)
        if operator == '+':
            print(f"Adding {to_compute} to total {total}")
            total += sum(to_compute)
            to_compute = []
            operator = None
        elif operator == '*':
            print(f"Multiplying {to_compute} to total {total}")
            prod = 1
            for x in to_compute:
                prod *= x
            total += prod
            to_compute = []
            operator = None
    return total

if __name__ == "__main__":
    input_data = read_input("2025/inputs/6.txt")
    transformed_data = transform_data(input_data)
    result_part1 = compute_result_part1(transformed_data)
    print(f"Result Part 1: {result_part1}")
    input_data_part2 = read_input_part2("2025/inputs/6.txt")
    print(compute_result_part2(input_data_part2))