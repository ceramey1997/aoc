file = open('input1.txt', 'r')

total = 0

def is_a_number(ch: str) -> bool:
    try:
        _ = int(ch)
        return True
    except ValueError:
        return False

def find_first_and_last(line : str) -> int:
    chars = [*line]
    nums_only = [ch for ch in chars if is_a_number(ch)]
    first = nums_only[0]
    last = nums_only[-1]
    totals = f"{first}{last}"
    return int(totals)

while True:
    line = file.readline()
    if not line:
        break
    lineInt = find_first_and_last(line)
    print(lineInt)
    total += lineInt
    lineInt = 0

print(total)
