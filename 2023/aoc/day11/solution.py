from dataclasses import dataclass
from aoc.utils.day import Day
from concurrent.futures import ThreadPoolExecutor, Future, as_completed

day = Day(11, "Cosmic Expansion")

@dataclass
class Galaxy():
    def __hash__(self):
        return hash(self.num)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.num == other.num
        return NotImplemented

    num: int
    x: int
    y: int

@dataclass
class GalaxyCombo:
    def __hash__(self):
        return hash(self.start.num + self.target.num)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            if self.start.num == other.start.num:
                return True
            if self.start.num == other.target.num:
                return True
            if self.target.num == other.target.num:
                return True
        return NotImplemented
    start: Galaxy
    target: Galaxy


class DoIt:
    def __init__(self, input: str):
        self.input = input
        #self.EXPANSION_CONSTANT = 1_000_000
    
    def solve_part_one(self):
        self.EXPANSION_CONSTANT = 1
        parsed_input: list[list[str]] = self.parse_input()
        galaxy = self.expand_galaxy(parsed_input)
        galaxy, galaxies = self.number_galaxies(galaxy)
        paths = self.find_paths(galaxy, galaxies)
        total = 0
        for p in paths:
            total += p[2]
        return total


    def parse_input(self) -> list[list[str]]:
        return [[i for i in l.strip()] for l in self.input.strip().split("\n")]

    def _transpose(self, l: list[list[str]]) -> list[list[str]]:
        return [list(row) for row in zip(*l)]

    #def _find_expansion_passes(self, galaxy: list[list[str]], galaxy_start: Galaxy, galaxy_target: Galaxy) -> tuple[int, int]:
    #    row_passes = galaxy[galaxy_start.x:galaxy_target.x].count(self.EXPANSION_CONSTANT)
    #    col = self._transpose(galaxy)[galaxy_start.y]
    #    col_passes = col[galaxy_start.y:galaxy_target.y].count(self.EXPANSION_CONSTANT)
    #    return row_passes, col_passes

    def expand_galaxy(self, starting_galaxy: list[list[str]]) -> list[list[str]]:
        starting_galaxy = self._expand_rows(starting_galaxy)
        transposed_gal = self._transpose(starting_galaxy)
        expanded_transpsed = self._expand_rows(transposed_gal)
        return self._transpose(expanded_transpsed)

    def _expand_rows(self, l: list[list[str]]) -> list[list[str]]:
        expansion_row = [self.EXPANSION_CONSTANT+1 for _ in l]
        i = 0
        while i < len(l):
            r = l[i]
            has_galaxies = "#" in r
            if not has_galaxies:
                l.insert(i, r)
                i += 2
            else:
                i += 1
        return l

    def number_galaxies(self, galaxy: list[list[str]]) -> tuple[list[list[str]], list[Galaxy]]:
        gals: list[Galaxy] = []
        galaxy_number = 1
        for idx, row in enumerate(galaxy):
            for col_idx, char in enumerate(row):
                if char == "#":
                    galaxy[idx][col_idx] = galaxy_number
                    gals.append(Galaxy(num=galaxy_number, x=idx, y=col_idx))
                    galaxy_number += 1
        return galaxy, gals
    
    def get_combos(self, galaxy: list[list[str]], galaxies: list[Galaxy]):
        combinations: list[GalaxyCombo] = []
        for idx, g in enumerate(galaxies):
            for g_2 in galaxies[idx+1:]:
                combinations.append(GalaxyCombo(g, g_2))
        return set(combinations)


    def find_paths(self, galaxy: list[list[str]], galaxies: list[Galaxy]):
        ret: list[tuple[galaxy, galaxy, int]] = []
        combinations = self.get_combos(galaxy, galaxies)
        with ThreadPoolExecutor() as exec:
            results: list[Future[tuple[Galaxy, Galaxy, int]]] = [exec.submit(self.find_path, combo.start, combo.target) for combo in combinations]
            for r in results:
                res = r.result()
                ret.append(res)
        return ret

    def find_path(self, start: Galaxy, target: Galaxy) -> tuple[Galaxy, Galaxy, int]:
        dist = abs(start.x - target.x) + abs(start.y - target.y)
        return start, target, dist

def part_one():
    file = open("aoc/day11/input1.txt", 'r')
    data = file.read()
    d = DoIt(data)
    return d.solve_part_one()


def part_two():
    return 0