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


def find_similarities(left: list[int], right: list[int]) -> list[tuple[int, int]]:
    hash: dict[int, int] = {}
    similarities: list[tuple[int, int]] = []
    for num in left:
        count_in_right = 0
        if num in hash:
            count_in_right = hash[num]
        else:
            count_in_right = right.count(num)
        similarities.append((num, count_in_right))
    return similarities


def get_similarity_scores(similarities: list[tuple[int, int]]) -> list[int]:
    return [sim[0] * sim[1] for sim in similarities]


def solve(scores: list[int]) -> int:
    solution = 0
    for score in scores:
        solution += score
    return solution


left, right = parse_file("input1.txt")
similarities = find_similarities(left, right)
scores = get_similarity_scores(similarities)
solution = solve(scores)
print(solution)
