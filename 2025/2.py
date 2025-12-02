def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()

def transform_data(data):
    ranges = []
    for range_str in data.split(','):
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))
    return ranges

def is_invalid_id(num, exactly=None):
    # check if number is made of a pattern repeated
    num_str = str(num)
    length = len(num_str)
    min_reps = exactly if exactly else 2
    # try all possible pattern lengths
    for pattern_len in range(1, length // min_reps + 1):
        # pattern must divide evenly into the number
        if length % pattern_len == 0:
            pattern = num_str[:pattern_len]
            repetitions = length // pattern_len
            # check if repeating the pattern recreates the full number
            if pattern * repetitions == num_str:
                if exactly:
                    if repetitions == exactly:
                        return True
                else:
                    if repetitions >= 2:
                        return True
    return False

def compute_result_part1(data):
    # find ids that are a pattern repeated exactly twice
    invalid_ids = []
    for start, end in data:
        for num in range(start, end + 1):
            if is_invalid_id(num, exactly=2):
                invalid_ids.append(num)
    return sum(invalid_ids)

def compute_result_part2(data):
    # find ids that are a pattern repeated at least twice (2 or more times)
    invalid_ids = []
    for start, end in data:
        for num in range(start, end + 1):
            if is_invalid_id(num):
                invalid_ids.append(num)
    return sum(invalid_ids)

if __name__ == "__main__":
    input_data = read_input("2025/inputs/2.txt")
    transformed_data = transform_data(input_data)

    result_part1 = compute_result_part1(transformed_data)
    print(f"Result Part 1: {result_part1}")

    result_part2 = compute_result_part2(transformed_data)
    print(f"Result Part 2: {result_part2}")
