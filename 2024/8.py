from math import gcd

class Point:
    def __init__(self, x, y, value=None):
        self.x = x
        self.y = y
        self.value = value

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def get_value(self):
        return self.value
    
    def set_value(self, value: str):
        self.value = value


def are_aligned(p1: Point, p2: Point, p3: Point):
    return (p1.x - p2.x) * (p1.y - p3.y) == (p1.y - p2.y) * (p1.x - p3.x)


def calculate_antinodes(p1: Point, p2: Point, grid_size):
    dx = p2.x - p1.x
    dy = p2.y - p1.y

    factor = gcd(abs(dx), abs(dy))
    dx //= factor
    dy //= factor

    antinode1 = Point(p1.x - dx, p1.y - dy)
    antinode2 = Point(p2.x + dx, p2.y + dy)

    def in_bounds(p):
        return 0 <= p.x < grid_size[0] and 0 <= p.y < grid_size[1]
    
    return [p for p in [antinode1, antinode2] if in_bounds(p)]


def points_aligned(p1: Point, p2: Point, grid_size):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    factor = gcd(abs(dx), abs(dy))
    dx //= factor
    dy //= factor

    points = []
    x, y = p1.x, p1.y
    while 0 <= x < grid_size[0] and 0 <= y < grid_size[1]:
        points.append(Point(x, y))
        x += dx
        y += dy

    x, y = p1.x - dx, p1.y - dy
    while 0 <= x < grid_size[0] and 0 <= y < grid_size[1]:
        points.append(Point(x, y))
        x -= dx
        y -= dy

    return points


class Grid:
    def __init__(self, file_path: str):
        self.grid = self.read_input(file_path)
        self.size = (len(self.grid), len(self.grid[0]))
        self.unique_chars = self.get_unique_chars()

    def read_input(self, file_path: str):
        with open(file_path) as file:
            return [
                [Point(i, j, value) for j, value in enumerate(line)]
                for i, line in enumerate(file.read().splitlines())
            ]

    def get_unique_chars(self):
        unique_chars = set()
        for row in self.grid:
            for point in row:
                if point.get_value() != '.':
                    unique_chars.add(point.get_value())
        return unique_chars

    def find_frequencies(self, frequency: str):
        points = []
        for row in self.grid:
            for point in row:
                if point.get_value() == frequency:
                    points.append(point)
        return points

    def find_all_antinodes(self):
        antinodes = set()

        for frequency in self.unique_chars:
            points = self.find_frequencies(frequency)

            for i, p1 in enumerate(points):
                for p2 in points[i + 1:]:
                    for antinode in calculate_antinodes(p1, p2, self.size):
                        antinodes.add((antinode.x, antinode.y))
        
        return antinodes

    def find_all_harmonic_antinodes(self):
        antinodes = set()

        for frequency in self.unique_chars:
            points = self.find_frequencies(frequency)

            for i, p1 in enumerate(points):
                for p2 in points[i + 1:]:
                    aligned = points_aligned(p1, p2, self.size)
                    antinodes.update((p.x, p.y) for p in aligned)
        
        return antinodes

    def __str__(self):
        return "\n".join(["".join([point.value for point in row]) for row in self.grid])

    def get_point(self, x: int, y: int):
        return self.grid[x][y]
    
    def set_point(self, x: int, y: int, value: str):
        self.grid[x][y].set_value(value)


if __name__ == "__main__":
    grid = Grid("inputs/input8.txt")

    antinodes = grid.find_all_antinodes()
    print(f"Nombre total d'antinode uniques : {len(antinodes)}")

    harmonic_antinodes = grid.find_all_harmonic_antinodes()
    print(f"Nombre total d'antinode harmoniques uniques : {len(harmonic_antinodes)}")
