def read_input(file_path):
    with open(file_path, "r") as file:
        # return it as a list of tuples of integers
        return [tuple(map(int, line.strip().split(","))) for line in file.readlines()]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Grid:
    def __init__(self, points: list[tuple[int, int]]):
        self.points = [Point(x, y) for x, y in points]
        self.width = max(point.x for point in self.points) + 1
        self.height = max(point.y for point in self.points) + 1

    def fill_points(self):
        self.grid = [['.' for _ in range(self.width)] for _ in range(self.height)]
        for point in self.points:
            self.grid[point.y][point.x] = '#'

    def is_point_on_edge(self, x, y):
        # check if point is on any edge defined by the points
        for i in range(len(self.points)):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % len(self.points)]
            if p1.x == p2.x and x == p1.x:
                if min(p1.y, p2.y) <= y <= max(p1.y, p2.y):
                    return True
            elif p1.y == p2.y and y == p1.y:
                if min(p1.x, p2.x) <= x <= max(p1.x, p2.x):
                    return True
        return False

    def is_point_inside(self, x, y):
        # ray-casting algorithm to check if point is inside polygon defined by the points
        n = len(self.points)
        inside = False
        j = n - 1
        for i in range(n):
            pi = self.points[i]
            pj = self.points[j]
            if ((pi.y > y) != (pj.y > y)) and (x < (pj.x - pi.x) * (y - pi.y) / (pj.y - pi.y) + pi.x):
                inside = not inside
            j = i
        return inside

    def is_valid_point(self, x, y):
        return self.is_point_on_edge(x, y) or self.is_point_inside(x, y)

    def display(self):
        self.fill_points()
        for row in self.grid:
            print(''.join(row))

    # we need to find in the grid which is the largest rectangle that have opposite corners as "#" this opposite corners can be either top-left and bottom-right or top-right and bottom-left
    def get_largest_rectangle(self):
        rectangle = ((),())
        max_area = 0
        for point in self.points:
            # find the farest point that is to its right
            for other in self.points:
                if other.x > point.x and other.y > point.y: # we're looking for bottom-right corner
                    area = (other.x - point.x + 1) * (other.y - point.y + 1) # add 1 to include the corners
                    if area > max_area:
                        max_area = area
                        rectangle = ((point.x, point.y), (other.x, other.y))
                if other.x < point.x and other.y > point.y: # we're looking for bottom-left corner
                    area = (point.x - other.x + 1) * (other.y - point.y + 1) # add 1 to include the corners
                    if area > max_area:
                        max_area = area
                        rectangle = ((other.x, other.y), (point.x, point.y))
        return rectangle[0], rectangle[1], max_area

    def is_rectangle_valid(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if not self.is_valid_point(x, y):
                    return False
        return True

    def get_largest_rectangle_no_obstacles(self):
        rectangle = ((), ())
        max_area = 0
        for point in self.points:
            for other in self.points:
                if other.x > point.x and other.y > point.y:
                    area = (other.x - point.x + 1) * (other.y - point.y + 1)
                    if area > max_area and self.is_rectangle_valid(point.x, point.y, other.x, other.y):
                        max_area = area
                        rectangle = ((point.x, point.y), (other.x, other.y))
                if other.x < point.x and other.y > point.y:
                    area = (point.x - other.x + 1) * (other.y - point.y + 1)
                    if area > max_area and self.is_rectangle_valid(other.x, point.y, point.x, other.y):
                        max_area = area
                        rectangle = ((other.x, point.y), (point.x, other.y))
        return rectangle[0], rectangle[1], max_area

def compute_result_part1(grid):
    return grid.get_largest_rectangle()

def compute_result_part2(grid):
    return grid.get_largest_rectangle_no_obstacles()

if __name__ == "__main__":
    points = read_input("2025/inputs/input.txt")
    grid = Grid(points)
    _, _, area = compute_result_part1(grid)
    print(f"Part 1: {area}")
    _, _, area_no_obs = compute_result_part2(grid)
    print(f"Part 2: {area_no_obs}")