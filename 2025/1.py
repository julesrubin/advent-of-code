def read_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines

def transform_data(data):
    transformed_data = []
    for item in data:
        direction, value = item[0], int(item[1:])
        if direction == 'L':
            value = -value
        transformed_data.append(value)
    return transformed_data

def compute_result_part1(data):
    # we start from position 0
    position = 50
    modulo = 100
    count = 0
    # then we iterate through each movement modulo 100
    for move in data:
        position = (position + move) % modulo
        if position == 0:
            count += 1
    return count


def compute_result_part2(data):
    position = 50
    modulo = 100
    # we now need to count how many time we pass THROUGH position 0
    count = 0
    for move in data:
        steps = abs(move)
        step_direction = 1 if move > 0 else -1
        for _ in range(steps):
            # not optimized at all but works :)
            position = (position + step_direction) % modulo
            if position == 0:
                count += 1
    return count

if __name__ == "__main__":
    input_lines = read_input("2025/inputs/1.txt")
    transformed_lines = transform_data(input_lines)
    result = compute_result_part1(transformed_lines)
    print(f"Result: {result}")
    result_part2 = compute_result_part2(transformed_lines)
    print(f"Result Part 2: {result_part2}")