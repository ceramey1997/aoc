
class Schematic:
    def __str__(self):
        gg = ""
        #for i in range(len(self._rows)):
        #    gg += f"{self._rows[i]}\n"
        total = 0
        for j in range(len(self._part_numbers)):
            total += self._part_numbers[j]
            #gg += f"{self._part_numbers[j]}\n"
        gg += f"****************{total}************"
        return gg

    def __init__(self):
        self._rows : list[list[str]] = []
        self._num_rows : int = 0
        self._part_numbers: list[int] = []

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
        if row_below >= len(self._rows):
            is_bottom = True 

        is_beginning = False
        is_end = False
        col_number = 0
        while col_number < len(self._rows[row_number]):
            start = col_number
            has_ints = False
            while True:
                try:
                    is_an_int = self.is_int(self._rows[row_number][col_number])
                    if not is_an_int:
                        break
                    has_ints = True
                    col_number += 1
                except Exception:
                    break

            if not has_ints:
                col_number += 1
                continue

            if start == 0:
                is_beginning = True

            if col_number == len(self._rows[row_number]):
                is_end = True

            # -1 for end cause col_number has been ++'d
            if self.has_symbol_around(row_number, start, col_number - 1, is_top, is_bottom, is_beginning, is_end):
                part_number = ""
                j = start
                while j < col_number:
                    #print(self._rows[row_number][j], end="")
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
                if j >= col_num_end and is_end:
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
                if k == col_num_start and is_beginning:
                    k += 1
                    continue
                if k >= col_num_end and is_end:
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

    def parse_line(self, line: str) -> list[str]:
        l = [*line]
        l.pop()
        return l



final = ItDoesThings('input1.txt')
print(final)


#    def has_symbol_adjacent(self, row_num: int, col_num: int) -> None:
#        return
#
#    def has_symbol_left(self, row_num: int, col_num: int) -> bool:
#        return False
#
#    def has_symbol_right(self, row_num: int, col_num: int) -> bool:
#        return False
#
#    def has_symbol_top(self, row_num: int, col_num: int) -> bool:
#        return False
#
#    def has_symbol_bottom(self, row_num: int, col_num: int) -> bool:
#        return False
