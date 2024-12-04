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
    patternn = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
    matches = patternn.findall(input)
    return matches


def get_multiples(matches: list[str]) -> list[tuple[int, int]]:
    multiples: list[tuple[int, int]] = []
    flag = True
    for match in matches:
        if match == "do()":
            flag = True
        elif match == "don't()":
            flag = False
        else:
            if flag:
                num1, num2 = map(int, match[4:-1].split(","))
                multiples.append((num1, num2))

    return multiples


def multiply_multiples(multiples: list[tuple[int, int]]) -> list[int]:
    mults = []
    for m in multiples:
        mults.append(m[0] * m[1])
    return mults


def add_together(multiples: list[int]) -> int:
    solution = 0
    for num in multiples:
        solution = solution + num
    return solution


def solve():
    txt = read_file("input2.txt")
    matches = sift(txt)
    multiples = get_multiples(matches)
    mults = multiply_multiples(multiples)
    return add_together(mults)


print(solve())
