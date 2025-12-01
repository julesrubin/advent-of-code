def read_input(file_path):
    with open(file_path) as f:
        data = f.read().strip()
    return data

def parse_input(data):
    rules, updates = data.split('\n\n')
    rules = [rule.split('|') for rule in rules.split('\n')]
    updates = updates.split('\n')
    return rules, updates

def check_rule(rule: list, update: str):
    first, second = rule
    if first in update and second in update:
        return update.index(first) < update.index(second)
    else:
        return True

def get_middle_number(update: str):
    update_array = update.split(",")
    return update_array[int(len(update_array) / 2)]

def correct_update(rules: list[list], update: str):
    update = update.split(",")
    for rule in rules:
        if not check_rule(rule, update):
            # get first and second strings in the rule
            first, second = rule
            # get the index of the first string in the update
            first_index = update.index(first)
            # get the index of the second string in the update
            second_index = update.index(second)
            # swap the two strings in the update
            update[first_index], update[second_index] = update[second_index], update[first_index]

    if not all(check_rule(rule, update) for rule in rules):
        return correct_update(rules, ",".join(update))
    else:
        return ",".join(update)
    
if __name__ == '__main__':
    data = read_input('inputs/input5.txt')
    rules, updates = parse_input(data)
    # part 1
    sum = 0
    for update in updates:
        if all(check_rule(rule, update) for rule in rules):
            sum += int(get_middle_number(update))
    print(sum)
    # part 2
    sum = 0
    for update in updates:
        if all(check_rule(rule, update) for rule in rules):
            pass
        else:
            new = correct_update(rules, update)
            # get the middle number of the list
            sum += int(get_middle_number(new))
    print(sum)