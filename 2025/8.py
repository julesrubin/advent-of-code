def read_input(file_path):
    with open(file_path, "r") as file:
        # return it as a list of tuples of integers
        return [tuple(map(int, line.strip().split(","))) for line in file.readlines()]


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Network:
    def __init__(self, points):
        self.points = points
        self.connections = []
        self.circuits = [[point] for point in points]

    def distance(self, p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2) ** 0.5

    def create_connection(self, p1, p2):
        self.connections.append((p1, p2))
        self.update_circuits(p1, p2)

    def update_circuits(self, p1, p2):
        circuit1 = None
        circuit2 = None
        for circuit in self.circuits:
            if p1 in circuit:
                circuit1 = circuit
            if p2 in circuit:
                circuit2 = circuit
        if circuit1 and circuit2 and circuit1 != circuit2:
            # merge circuits
            circuit1.extend(circuit2)
            self.circuits.remove(circuit2)
            # ensure uniqueness
            circuit1 = list(set(circuit1))
        elif circuit1:
            if p2 not in circuit1:
                circuit1.append(p2)
        elif circuit2:
            if p1 not in circuit2:
                circuit2.append(p1)
        else:
            self.circuits.append([p1, p2])

    def order_closest_pairs(self):
        pairs = []
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                p1 = self.points[i]
                p2 = self.points[j]
                dist = self.distance(p1, p2)
                pairs.append((dist, p1, p2))
        pairs.sort(key=lambda x: x[0])
        return pairs


def compute_result_part1(points, example_mode=False):
    # example mode is an easy way to switch from example to real input
    nb_pairs = 10 if example_mode else 1000
    network = Network(points)
    ordered_pairs = network.order_closest_pairs()
    # connect the 10 shortest pairs
    for i in range(nb_pairs):
        dist, p1, p2 = ordered_pairs[i]
        network.create_connection(p1, p2)
    # return the product of lenght of the top 3 longest circuits
    top_circuits = sorted(network.circuits, key=lambda c: len(c), reverse=True)[:3]
    result = 1
    for circuit in top_circuits:
        result *= len(circuit)
        print(f"Circuit with {len(circuit)} points.")
    return result


def compute_result_part2(points):
    network = Network(points)
    ordered_pairs = network.order_closest_pairs()

    # with this nested loop we do not have optimized performance but it is simpler to implement
    while len(network.circuits) > 1:
        for dist, p1, p2 in ordered_pairs:
            circuit1 = None
            circuit2 = None
            for circuit in network.circuits:
                if p1 in circuit:
                    circuit1 = circuit
                if p2 in circuit:
                    circuit2 = circuit
            if circuit1 != circuit2:
                network.create_connection(p1, p2)
                break
    return p1.x * p2.x


if __name__ == "__main__":
    input_data = read_input("2025/inputs/8.txt")
    points = [Point(x, y, z) for x, y, z in input_data]
    result = compute_result_part1(points, example_mode=False)
    print("Part 1:", result)
    result = compute_result_part2(points)
    print("Part 2:", result)
