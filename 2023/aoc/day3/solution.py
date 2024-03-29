from aoc.utils.day import Day

day = Day(3, "Gear Ratios")

def part_one():
    class Schematic:
        def __str__(self):
            gg = ""
            total = 0
            for j in range(len(self._part_numbers)):
                total += self._part_numbers[j]
            gg += f"****************{total}************"
            return gg
    
        def __init__(self):
            self._rows : list[list[str]] = []
            self._num_rows : int = 0
            self._part_numbers: list[int] = []
            self.total = 0

        def calculate_total(self):
            for j in self._part_numbers:
                self.total += j
    
        def build_row(self, new_row : list[str]) -> None:
            self._rows.append(new_row)
            self._num_rows += 1
        
        def analyze(self):
            for i in range(len(self._rows)):
                self.analyze_row(i)
    
        def analyze_row(self, row_number: int):
            row_above = row_number - 1
            row_below = row_number + 1
            is_top = False
            is_bottom = False
            if row_above < 0:
                is_top = True
            if row_below >= len(self._rows)-1:
                is_bottom = True 
    
            col_number = 0
            while col_number <= len(self._rows[row_number]):
                is_beginning = False
                is_end = False
                start = col_number
                my_int = "" 
                while True:
                    try:
                        is_an_int = self.is_int(self._rows[row_number][col_number])
                        if not is_an_int:
                            break
                        my_int += self._rows[row_number][col_number]
                        col_number += 1
                    except Exception:
                        break
    
                if my_int == "":
                    col_number += 1
                    my_int = ""
                    continue
    
                if start == 0:
                    is_beginning = True
    
                if col_number == len(self._rows[row_number]):
                    is_end = True
    
                # -1 for end cause col_number has been ++'d
                if self.has_symbol_around(row_number, start, col_number-1, is_top, is_bottom, is_beginning, is_end):
                    part_number = ""
                    j = start
                    while j < col_number:
                        part_number += self._rows[row_number][j]
                        j += 1
                    self._part_numbers.append(int(part_number))
                    part_number = ""
                col_number += 1
    
        def is_int(self, char) -> bool:
            try:
                int(char)
                return True
            except Exception:
                return False
    
        def has_symbol_around(self, row_number: int, col_num_start: int, col_num_end: int, is_top: bool, is_bottom: bool, is_beginning: bool, is_end: bool) -> bool:
            if not is_beginning:
                if self._rows[row_number][col_num_start - 1] != '.' and not self.is_int(self._rows[row_number][col_num_start - 1]):
                    return True
            if not is_end:
                if self._rows[row_number][col_num_end + 1] != '.' and not self.is_int(self._rows[row_number][col_num_end + 1]):
                    return True
            if not is_top:
                j = col_num_start
                if not is_beginning:
                    j = col_num_start - 1
                while j <= col_num_end + 1:
                    if j == col_num_start and is_beginning:
                        j += 1
                        continue
                    if j > col_num_end and is_end:
                        j += 1
                        continue
                    if self._rows[row_number - 1][j] != '.' and not self.is_int(self._rows[row_number - 1][j]):
                        return True
                    j += 1
            if not is_bottom:
                k = col_num_start
                if not is_beginning:
                    k = col_num_start - 1
                while k <= col_num_end + 1:
                    if k > col_num_end and is_end:
                        k += 1
                        continue
                    if self._rows[row_number + 1][k] != '.' and not self.is_int(self._rows[row_number + 1][k]):
                        return True
                    k += 1
            return False
    
    
    
    class ItDoesThings:
        def __str__(self):
            return str(self._schematic) 
        def __init__(self, fileName : str):
            file = open(fileName, 'r')
            self._schematic = Schematic()
            while True:
                line = file.readline()
                if not line:
                    break
                self._schematic.build_row(self.parse_line(line))
            
            self._schematic.analyze()
            self._schematic.calculate_total()
    
        def parse_line(self, line: str) -> list[str]:
            l = [*line]
            l.pop()
            return l
    
    
    
    final = ItDoesThings('aoc/day3/input1.txt')
    return final._schematic.total



def part_two():
    class Gear:
        def __str__(self):
            return f"{self.n1} * {self.n2} = {self.ratio}"
    
        def __init__(self, n1: int, n2: int):
            self.n1 = n1
            self.n2 = n2
            self.ratio = n1 * n2
    
    class Schematic:
        def __str__(self):
            total = 0
            gg = ""
            for g in self._gears:
                total += g.ratio
                gg += f"{g}\n"
    
            gg += f"**********{total}***********"
            return gg
    
        def __init__(self):
            self._rows : list[list[str]] = []
            self._num_rows : int = 0
            self._part_numbers: list[int] = []
            self._gears: list[Gear] = []
            self.total = 0

        def calculate_total(self):
            for g in self._gears:
                self.total += g.ratio
    
        def build_row(self, new_row : list[str]) -> None:
            self._rows.append(new_row)
            self._num_rows += 1
        
        def analyze(self):
            for i in range(len(self._rows)):
                self.analyze_row_part2(i)
    
    
        def analyze_row_part2(self, row_number: int):
            col_num = 0
            while col_num < len(self._rows[row_number]):
                if self._rows[row_number][col_num] == "*":
                    n = self.nums_around(row_number, col_num)
                    if len(n) == 2:
                        g = Gear(n[0], n[1])
                        self._gears.append(g)
                col_num += 1
    
        def nums_around(self, row_number : int, col_number : int) -> list[int]:
            left = self.nums_left(row_number, col_number-1)
            right = self.nums_right(row_number, col_number+1)
            above = self.nums_above(row_number, col_number)
            below = self.nums_below(row_number, col_number)
            res = []
            for i in left:
                res.append(i)
            for j in right:
                res.append(j)
            for k in above:
                res.append(k)
            for l in below:
                res.append(l)
            if len(res) > 2:
                return []
            else:
                return res
    
        def nums_above(self, row_number : int, col_number : int) -> list[int]:
            row = row_number - 1
            if row < 0:
                return []
            my_int = ""
    
            try:
                is_an_int = self.is_int(self._rows[row][col_number])
                if is_an_int != "":
                    my_int = self.num_find_when_directly_above_or_below(row, col_number)
            except Exception:
                pass
    
            res = []
            if my_int != "":
                res.append(int(my_int))
                return res
    
            left_above = self.nums_left(row, col_number - 1)
            right_above = self.nums_right(row, col_number + 1)
            for i in left_above:
                res.append(i)
            for j in right_above:
                res.append(j)
            return res 
    
        def nums_below(self, row_number : int, col_number : int) -> list[int]:
            row = row_number + 1
            if row >= len(self._rows):
                return []
            my_int = ""
            try:
                is_an_int = self.is_int(self._rows[row][col_number])
                if is_an_int != "":
                    my_int = self.num_find_when_directly_above_or_below(row, col_number)
            except Exception:
                pass
    
            res = []
            if my_int != "":
                res.append(int(my_int))
                return res
            left_below = self.nums_left(row, col_number - 1)
            right_below = self.nums_right(row, col_number + 1)
            for i in left_below:
                res.append(i)
            for j in right_below:
                res.append(j)
            return res 
    
        def nums_left(self, row_number : int, col_number : int) -> list[int]:
            my_int = ""
            while True:
                try:
                    is_an_int = self.is_int(self._rows[row_number][col_number])
                    if is_an_int == "":
                        break
                    my_int += is_an_int
                    col_number -= 1
                    if col_number < 0:
                        break
                except Exception:
                    break
            if my_int != "":
                return [int(my_int[::-1])]
            return []
    
        def nums_right(self, row_number : int, col_number : int) -> list[int]:
            my_int = ""
            while True:
                try:
                    is_an_int = self.is_int(self._rows[row_number][col_number])
                    if is_an_int == "":
                        break
                    my_int += is_an_int
                    col_number += 1 
                    if col_number >= len(self._rows[row_number]):
                        break
                except Exception:
                    break
            if my_int != "":
                return [int(my_int)]
            return []
    
        def is_int(self, char) -> str:
            try:
                int(char)
                return char
            except Exception:
                return ""
    
        def num_find_when_directly_above_or_below(self, row_num : int, col_num : int) -> int:
            start = col_num
            while True:
                try:
                    is_an_int = self.is_int(self._rows[row_num][col_num])
                    if (is_an_int == ""):
                        break
                    start = col_num
                    col_num -= 1
                except Exception:
                    break
            end = start
            num = ""
            while True:
                try:
                    is_an_int = self.is_int(self._rows[row_num][end])
                    if (is_an_int == ""):
                        break
                    num += self._rows[row_num][end]
                    end += 1 
                except Exception:
                    break
            return int(num)
    
    class ItDoesThings:
        def __str__(self):
            return str(self._schematic) 
        def __init__(self, fileName : str):
            file = open(fileName, 'r')
            self._schematic = Schematic()
            while True:
                line = file.readline()
                if not line:
                    break
                self._schematic.build_row(self.parse_line(line))
            
            self._schematic.analyze()
            self._schematic.calculate_total()
    
        def parse_line(self, line: str) -> list[str]:
            l = [*line]
            l.pop()
            return l
    
    
    
    final = ItDoesThings('aoc/day3/input2.txt')
    return final._schematic.total
