def parse_file(filename: str) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []
    file = open(filename, "r")
    while True:
        line = file.readline()
        if not line:
            break
        split_line = line.split("   ")
        left.append(int(split_line[0]))
        right.append(int(split_line[1]))
    return left, right


def create_pairs(left: list[int], right: list[int]) -> list[tuple[int, int]]:
    pairs = []
    left.sort()
    right.sort()
    if len(left) != len(right):
        raise Exception("left must match right length")
    i = 0
    while True:
        if i == len(left):
            break
        pairs.append((left[i], right[i]))
        i = i + 1
    return pairs


def find_distances(pairs: list[tuple[int, int]]) -> list[int]:
    distances = []
    for pair in pairs:
        distances.append(abs((pair[0] - pair[1])))
    return distances


def solve(distances: list[int]) -> int:
    solution = 0
    for distance in distances:
        solution += distance
    return solution


left, right = parse_file("input1.txt")
pairs = create_pairs(left, right)
distances = find_distances(pairs)
solution = solve(distances)
print(solution)
