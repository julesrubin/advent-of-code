import re

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()
    
def compute_sum_part_1(text):
    pattern = re.compile(r"mul\((\d+),\s*(\d+)\)")
    return sum(int(x) * int(y) for x, y in re.findall(pattern, text))

def compute_sum_part_2(text):
    import re
    exp = r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))"
    total_sum = 0
    matches = re.findall(exp, text)
    state = True
    for match in matches:
        if match[2] == "do()":
            state = True
        elif match[3] == "don't()":
            state = False
        elif state:
            total_sum += int(match[0]) * int(match[1])
    return total_sum



if __name__ == "__main__":
    file_path = "inputs/input3.txt"
    text = read_input_file(file_path)
    print(compute_sum_part_1(text))
    print(compute_sum_part_2(text))
