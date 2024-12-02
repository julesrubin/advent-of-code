def read_input(file_path):
    reports = []
    with open(file_path, "r") as file:
        for line in file:
            reports.append(list(map(int, line.split())))

    return reports

def is_safe_report(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    if not all(1 <= abs(diff) <= 3 for diff in differences):
        return False
    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        return True
    return False

def is_safe_with_dampener(report):
    if is_safe_report(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    return False

if __name__ == "__main__":
    file_path = "inputs/input2.txt"
    reports = read_input(file_path)
    safe_reports_count = sum(is_safe_report(report) for report in reports)
    safe_reports_with_dampener_count = sum(is_safe_with_dampener(report) for report in reports)

    print("Number of safe reports:", safe_reports_count)
    print("Number of safe reports with the Problem Dampener:", safe_reports_with_dampener_count)