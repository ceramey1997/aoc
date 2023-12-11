from enum import Enum
from collections import deque


class P(Enum):
    VERTICAL_NORTH_SOUTH = 0
    HORTIZONTAL_EAST_WEST = 1
    BEND90_NORTH_EAST = 2
    BEND90_NORTH_WEST = 3
    BEND90_SOUTH_WEST = 4
    BEND90_SOUTH_EAST = 5

pipe_to_str = {
    P.VERTICAL_NORTH_SOUTH: "|",
    P.HORTIZONTAL_EAST_WEST: "-",
    P.BEND90_NORTH_EAST: "L",
    P.BEND90_NORTH_WEST: "J",
    P.BEND90_SOUTH_WEST: "7",
    P.BEND90_SOUTH_EAST: "F"
}
str_to_pipe = {
    "|": P.VERTICAL_NORTH_SOUTH,
    "-": P.HORTIZONTAL_EAST_WEST,
    "L": P.BEND90_NORTH_EAST,
    "J": P.BEND90_NORTH_WEST,
    "7": P.BEND90_SOUTH_WEST,
    "F": P.BEND90_SOUTH_EAST, 
}

class D(Enum):
    WEST = 0 # left
    EAST = 1 # right
    NORTH = 2 # up
    SOUTH = 3 # down

class Pipe:
    def __str__(self):
        return f"{self.pipe}"

    def __init__(self, pipe: str, row_num: int, col_num: int, len_rows: int, len_col: int, pipe_type: P | None = None):
        self._row_num = row_num
        self._col_num = col_num
        self._len_rows = len_rows
        self._len_col = len_col

        self.pipe = pipe
        self.is_ground: bool = pipe == "."
        self.is_start: bool = pipe == "S"
        self.p_enum: P | None = None
        self.possible_directions: list[D] | None = None

        if pipe_type != None:
            self.p_enum = pipe_type
            self.pipe = pipe_to_str[pipe_type]
        if not self.is_ground and self.pipe != "S":
            self.p_enum, self.possible_directions = self.define_pipe()

    def direction_in_possibles(self, direction: D):
        if self.possible_directions == None:
            raise Exception(f"Pipe has no possibles {self.pipe}")
        return direction in self.possible_directions


    def determine_possible_directions(self, dir: list[D]) -> list[D]:
        possible_directions: list[D] = []
        for d in dir:
            match d:
                case D.NORTH:
                    if self._row_num != 0:
                        possible_directions.append(d)
                case D.SOUTH:
                    if self._row_num != self._len_rows - 1:
                        possible_directions.append(d)
                case D.WEST:
                    if self._col_num != 0:
                        possible_directions.append(d)
                case D.EAST:
                    if self._col_num != self._len_col - 1:
                        possible_directions.append(d)
        if len(possible_directions) > 2:
            raise Exception("cannot have more than 2 possible directions")
        return possible_directions

    def define_pipe(self) -> tuple[P, list[D]]:
        match self.pipe:
            case "|":
                return P.VERTICAL_NORTH_SOUTH, self.determine_possible_directions([D.NORTH, D.SOUTH])
            case "-":
                return P.HORTIZONTAL_EAST_WEST, self.determine_possible_directions([D.WEST, D.EAST])
            case "L":
                return P.BEND90_NORTH_EAST, self.determine_possible_directions([D.NORTH, D.EAST])
            case "J":
                return P.BEND90_NORTH_WEST , self.determine_possible_directions([D.NORTH, D.WEST])
            case "7":
                return P.BEND90_SOUTH_WEST, self.determine_possible_directions([D.SOUTH, D.WEST])
            case "F":
                return P.BEND90_SOUTH_EAST, self.determine_possible_directions([D.SOUTH, D.EAST])
            case ".":
                raise Exception(". is ground and shouldn't be evaluated")
            case "S":
                raise Exception("S is the starting position and shouldn't be evaluated")
            case _:
                raise Exception(f"unknown pipe character given \"{self.pipe}\"")


class DoingIt:
    def __str__(self):
        s = ""
        for l in self.map:
            for p in l:
                s += f"{p}"
            s += "\n"

        s += f"\nFurthest Point: {self.furthest_point}"
        s += f"\nEnclosed Points: {self.enclosed}"
        return s

    def __init__(self, fileName: str):
        file = open(fileName, 'r')
        self.str_map: list[list[str]] = [[*l] for l in file.read().strip().split("\n")]

        len_rows = len(self.str_map)
        len_col = len(self.str_map[0])
        start_row_num, start_col_idx =self.find_s()

        self.map: list[list[Pipe]] = [[Pipe(pipe=char, row_num=row_num, col_num=col_num, len_rows=len_rows, len_col=len_col) for col_num, char in enumerate(l)] for row_num, l in enumerate(self.str_map)]
        start_pipe = self.determine_start_type(start_row_num, start_col_idx)
        self.map[start_row_num][start_col_idx] = Pipe(pipe="S", row_num=start_row_num, col_num=start_col_idx, len_rows=len_rows, len_col=len_col, pipe_type=start_pipe)
        self.furthest_point, loop_nodes = self.traverse(start_row_num, start_col_idx)
        outside_nodes = self.map_areas_horizontal()

        self.enclosed = len(self.map) * len(self.map[0]) - len(outside_nodes | loop_nodes)

    def map_areas_horizontal(self) -> set[tuple[int, int]]:
        outside : set[tuple[int, int]] = set()
        for row_num, row in enumerate(self.map):
            within = False
            up = None
            for col_idx, pipe in enumerate(row):
                if pipe.p_enum == P.VERTICAL_NORTH_SOUTH:
                    assert up is None
                    within = not within
                elif pipe.p_enum == P.HORTIZONTAL_EAST_WEST:
                    assert up is not None
                elif pipe.p_enum in [P.BEND90_NORTH_EAST, P.BEND90_SOUTH_EAST]:
                    assert up is None
                    up = pipe.p_enum == P.BEND90_NORTH_EAST
                elif pipe.p_enum in [P.BEND90_SOUTH_WEST, P.BEND90_NORTH_WEST]:
                    assert up is not None
                    if pipe.p_enum != (P.BEND90_NORTH_WEST if up else P.BEND90_SOUTH_WEST):
                        within = not within
                    up = None
                else:
                    if pipe.is_ground:
                        pass
                    else:
                        raise Exception(f"bad horizontal {pipe.pipe}")
                if not within:
                    outside.add((row_num, col_idx))
        self.replace_for_visuals(outside)
        return outside

    def replace_for_visuals(self, outsides: set[tuple[int, int]]) -> set[tuple[int, int]]:
        insides: set[tuple[int, int]] = set()
        for row_num, row in enumerate(self.map):
            for col_idx, pipe in enumerate(row):
                if pipe.is_ground and (row_num, col_idx) in outsides:
                    pipe.pipe = "0"
                elif  pipe.is_ground and (row_num, col_idx) not in outsides:
                    pipe.pipe = "I"
        return insides 

    def traverse(self, start_row: int, start_col: int) -> tuple[int, set[tuple[int, int]]]:
        seen: set[tuple[int, int]] = {(start_row, start_col)}
        queue: deque[tuple[int, int]] = deque([(start_row, start_col)])
        while queue:
            row, col = queue.popleft()
            current_pipe: Pipe = self.map[row][col]
            if current_pipe.direction_in_possibles(D.NORTH) and (row-1, col) not in seen: # extra condition to not duplicate work
                north_pipe = self.map[row-1][col]
                if north_pipe.direction_in_possibles(D.SOUTH):
                    seen.add((row-1, col))
                    queue.append((row-1, col))
            if current_pipe.direction_in_possibles(D.SOUTH) and (row+1, col) not in seen:
                south_pipe = self.map[row+1][col]
                if south_pipe.direction_in_possibles(D.NORTH):
                    seen.add((row+1, col))
                    queue.append((row+1, col))
            if current_pipe.direction_in_possibles(D.EAST) and (row, col+1) not in seen:
                east_pipe = self.map[row][col+1]
                if east_pipe.direction_in_possibles(D.WEST):
                    seen.add((row, col+1))
                    queue.append((row, col+1))
            if current_pipe.direction_in_possibles(D.WEST) and (row, col-1) not in seen:
                west_pipe = self.map[row][col-1]
                if west_pipe.direction_in_possibles(D.EAST):
                    seen.add((row, col-1))
                    queue.append((row, col-1))
        self.remove_unnecessary_pipes_from_map(seen)
        return len(seen) // 2, seen

    def remove_unnecessary_pipes_from_map(self, loop_pipe_list: set[tuple[int, int]]) -> None:
        for row_num, row in enumerate(self.map):
            for col_idx, pipe in enumerate(row):
                if (row_num, col_idx) not in loop_pipe_list:
                    pipe.pipe = "."
                    pipe.is_ground = True
                    pipe.p_enum = None
                    pipe.possible_directions = None

    def find_s(self) -> tuple[int, int]:
        for row_num, row in enumerate(self.str_map):
            for col_idx, column in enumerate(row):
                if column == "S":
                    return row_num, col_idx 
        raise Exception("S not found in map")

    def determine_start_type(self, s_row: int, s_col: int) -> P:
        possible_directions = []
        north: Pipe | None = None
        south: Pipe | None = None
        east: Pipe | None = None
        west: Pipe | None = None

        north_possible: bool = False
        south_possible: bool = False 
        east_possible: bool = False
        west_possible: bool = False

        if s_row != 0:
            north = self.map[s_row-1][s_col]
            if north.possible_directions != None and D.SOUTH in north.possible_directions:
                possible_directions.append(D.NORTH)
                north_possible = True
        if s_row != len(self.map) - 1:
            south = self.map[s_row+1][s_col]
            if south.possible_directions != None and D.NORTH in south.possible_directions:
                possible_directions.append(D.SOUTH)
                south_possible = True
        if s_col != 0:
            west = self.map[s_row][s_col-1]
            if west.possible_directions != None and D.EAST in west.possible_directions:
                possible_directions.append(D.WEST)
                west_possible = True
        if s_col != len(self.map[s_row]) - 1:
            east = self.map[s_row][s_col+1]
            if east.possible_directions != None and D.WEST in east.possible_directions:
                possible_directions.append(D.EAST)
                east_possible = True

        s_pipe_type = self._type_from_direction(north_possible, south_possible, east_possible, west_possible)
        return s_pipe_type

    def _type_from_direction(self, north: bool, south: bool, east: bool, west: bool) -> P:
        if north and south:
            return P.VERTICAL_NORTH_SOUTH
        if east and west:
            return P.HORTIZONTAL_EAST_WEST
        if north and east:
            return P.BEND90_NORTH_EAST
        if north and west:
            return P.BEND90_NORTH_WEST
        if south and west:
            return P.BEND90_SOUTH_WEST
        if south and east:
            return P.BEND90_SOUTH_EAST
        raise Exception("should have found S starting type")

final = DoingIt("input2.txt")
print(final)
