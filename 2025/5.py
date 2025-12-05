def read_input(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    
    parts = content.strip().split("\n\n")
    ranges_part = parts[0].splitlines()
    ids_part = parts[1].splitlines()
    
    ranges = []
    for line in ranges_part:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))
        
    ids = []
    for line in ids_part:
        ids.append(int(line))
        
    return ranges, ids

def is_fresh(ingredient_id, ranges):
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False

def compute_result_part1(ranges, ids):
    fresh_count = 0
    for ingredient_id in ids:
        if is_fresh(ingredient_id, ranges):
            fresh_count += 1
    return fresh_count

def compute_result_part2(ranges):
    if not ranges:
        return 0
    
    # Sort ranges by start value
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    
    merged_ranges = []
    current_start, current_end = sorted_ranges[0]
    
    for i in range(1, len(sorted_ranges)):
        next_start, next_end = sorted_ranges[i]
        
        if next_start <= current_end + 1: # Overlap or adjacent
            current_end = max(current_end, next_end)
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = next_start, next_end
            
    merged_ranges.append((current_start, current_end))
    
    total_fresh = 0
    for start, end in merged_ranges:
        total_fresh += (end - start + 1)
        
    return total_fresh

if __name__ == "__main__":
    ranges, ids = read_input("2025/inputs/5.txt")
    result_part1 = compute_result_part1(ranges, ids)
    print(f"Result Part 1: {result_part1}")
    result_part2 = compute_result_part2(ranges)
    print(f"Result Part 2: {result_part2}")
