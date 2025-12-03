def read_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines

def find_max_joltage(bank, k=2):
    if k == 2:
        # for 2 batteries: try all pairs
        max_joltage = 0
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                joltage = int(bank[i] + bank[j])
                max_joltage = max(max_joltage, joltage)
        return max_joltage

    # general case: selection for k batteries
    n = len(bank)
    selected = []
    start = 0
    for pos in range(k):
        # how many more do we need after this?
        remaining = k - pos - 1
        # latest index we can pick from
        window_end = n - remaining
        # find max digit in valid window
        best_digit = bank[start]
        best_idx = start
        for i in range(start, window_end):
            if bank[i] > best_digit:
                best_digit = bank[i]
                best_idx = i
        selected.append(best_digit)
        start = best_idx + 1
    return int(''.join(selected))

def compute_result_part1(data):
    # find max joltage by selecting exactly 2 batteries per bank
    total_joltage = 0
    for bank in data:
        if bank:
            total_joltage += find_max_joltage(bank)
    return total_joltage

def compute_result_part2(data):
    # find max joltage by selecting exactly 12 batteries per bank
    total_joltage = 0
    for bank in data:
        if bank:
            total_joltage += find_max_joltage(bank, 12)
    return total_joltage

if __name__ == "__main__":
    input_lines = read_input("2025/inputs/3.txt")
    result = compute_result_part1(input_lines)
    print(f"Result Part 1: {result}")
    result_part2 = compute_result_part2(input_lines)
    print(f"Result Part 2: {result_part2}")
