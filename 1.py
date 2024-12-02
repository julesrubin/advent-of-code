from collections import Counter

def read_input(file_path):
    # Initialize the lists
    left_list = []
    right_list = []

    # Process the file to extract the lists
    with open(file_path, "r") as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

def compute_similarity_score(left_list, right_list):
    # Step 1: Count occurrences of each number in the right list
    right_list_counts = Counter(right_list)

    # Step 2: Calculate the similarity score
    similarity_score = sum(left * right_list_counts[left] for left in left_list)

    return similarity_score

if __name__ == "__main__":
    file_path = "inputs/input1.txt"
    left_list, right_list = read_input(file_path)
    similarity_score = compute_similarity_score(left_list, right_list)
    print(similarity_score)
