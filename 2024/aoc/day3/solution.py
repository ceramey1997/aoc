import re


def read_file(filename: str) -> str:
    file = open(filename, "r")
    txt = ""
    while True:
        line = file.readline()
        if not line:
            break
        txt = txt + line
    return txt


def sift(input: str) -> list[str]:
    pattern = re.compile(r"(mul\(\d{1,3},\d{1,3}\))")
    matches: list[str] = pattern.findall(input)
    return matches


def parse_matches(matches: list[str]) -> list[int]:
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    multiples: list[int] = []
    for match in matches:
        nums = pattern.findall(match)
        multiples.append((int(nums[0][0]) * int(nums[0][1])))
    return multiples


def add_together(multiples: list[int]) -> int:
    solution = 0
    for num in multiples:
        solution = solution + num
    return solution


txt = read_file("input1.txt")
matches = sift(txt)
multiples = parse_matches(matches)
solution = add_together(multiples)
print(solution)
