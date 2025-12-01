def read_input(file_path):
    with open(file_path) as f:
        file = f.read().strip().splitlines()
    data = [
        {
            int(file[i].split(":")[0]): [
                int(num) for num in file[i].split(":")[1].strip().split(" ")
            ]
        }
        for i in range(len(file))
    ]
    return data


def compute_equation(equation: str) -> int:
    equation = equation.split(" ")
    result = int(equation[0])
    for i in range(1, len(equation), 2):
        if equation[i] == "+":
            result += int(equation[i + 1])
        elif equation[i] == "*":
            result *= int(equation[i + 1])
        elif equation[i] == "||":
            result = int(str(result) + str(equation[i + 1]))
    return result


def is_valid(key: int, value: list, operations: list = [" * ", " + "]) -> bool:
    import itertools

    for op in itertools.product(operations, repeat=len(value) - 1):
        equation = [str(value[i]) + op[i] for i in range(len(value) - 1)] + [
            str(value[-1])
        ]
        equation = "".join(equation)
        result = compute_equation(equation)
        if result == key:
            return True

    return False


def get_sum(operations: list = [" * ", " + "]) -> int:
    sum_ = 0
    for d in data:
        for key, value in d.items():
            if is_valid(key=key, value=value, operations=operations):
                sum_ += key
    return sum_


if __name__ == "__main__":
    file_path = "inputs/input7.txt"
    data = read_input(file_path)
    print(get_sum())
    print(get_sum(operations=[" * ", " + ", " || "]))
