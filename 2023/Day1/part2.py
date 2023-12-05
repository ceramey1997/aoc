file = open('input2.txt', 'r')

total = 0

int_str = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def index_starts_number(idx: int, line: str) -> int | None:
    for str_num, num in int_str.items():
        find_num = line.find(str_num, idx, len(line))
        if find_num != -1:
            if find_num == idx:
                return num;
    return None

def is_a_number(idx: int, ch: str, line: str) -> int | None:
    try:
        num = int(ch)
        return num
    except ValueError:
        num_found = index_starts_number(idx, line)
        if num_found != None:
            return num_found

def find_first_and_last(line : str) -> int:
    chars = [*line]
    nums_only = []
    for i in range(len(chars)):
        potential_num = is_a_number(i, chars[i], line)
        if potential_num != None:
            nums_only.append(potential_num)
    first = nums_only[0]
    last = nums_only[-1]
    totals = f"{first}{last}"
    return int(totals)

while True:
    line = file.readline()
    if not line:
        break
    lineInt = find_first_and_last(line)
    total += lineInt
    lineInt = 0

print(total)
