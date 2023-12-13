from aoc.day11.solution import DoIt, Galaxy, GalaxyCombo


def test_part1():
    test_input = """....
...#
#...
...."""
    res = DoIt(test_input)
    parsed = res.parse_input()
    res.EXPANSION_CONSTANT = 1
    expanded: list[str[str]] = res.expand_galaxy(parsed)
    assert expanded == [
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def test_transpose():
    test_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
    input = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]]
    res = DoIt(test_input)
    result = res._transpose(input)
    assert result == [[1,1,1,1,1,1], [2,2,2,2,2,2], [3,3,3,3,3,3], [4,4,4,4,4,4]]

def test_count_galaxies():
    test_input = """.....
.#..#
#..#.
..#.."""
    res = DoIt(test_input)
    res.EXPANSION_CONSTANT = 1
    parsed = res.parse_input()
    counted, gals = res.number_galaxies(parsed)
    assert counted == [['.', '.', '.', '.', '.'],
                       ['.',  1 , '.', '.',  2 ],
                       [ 3 , '.', '.',  4 , '.'],
                       ['.', '.',  5 , '.', '.']]

    assert gals[0].num == 1 and gals[0].x == 1 and gals[0].y == 1
    assert gals[1].num == 2 and gals[1].x == 1 and gals[1].y == 4
    assert gals[2].num == 3 and gals[2].x == 2 and gals[2].y == 0
    assert gals[3].num == 4 and gals[3].x == 2 and gals[3].y == 3
    assert gals[4].num == 5 and gals[4].x == 3 and gals[4].y == 2

def test_find_path():
    test_input = """.....
.#..#
#..#.
..#.."""
    res = DoIt(test_input)
    res.EXPANSION_CONSTANT = 1
    parsed = res.parse_input()
    _, gals = res.number_galaxies(parsed)
    distance1to2 = res.find_path(gals[0], gals[1])
    assert distance1to2[2] == 3


def test_find_path2():
    test_input = """....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""

    res = DoIt(test_input)
    res.EXPANSION_CONSTANT = 1
    parsed = res.parse_input()
    galaxy, gals = res.number_galaxies(parsed)
    distance5to9 = res.find_path(gals[4], gals[8])
    distance1to7 = res.find_path(gals[0], gals[6])
    distance3to6 = res.find_path(gals[2], gals[5])
    distance7to8 = res.find_path(gals[7], gals[8])
    assert distance5to9[2] == 9
    assert distance1to7[2] == 15
    assert distance3to6[2] == 17
    assert distance7to8[2] == 5



def test_find_path2():
    test_input = """....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""

    res = DoIt(test_input)
    res.EXPANSION_CONSTANT = 1
    parsed = res.parse_input()
    _, gals = res.number_galaxies(parsed)
    distance5to9 = res.find_path(gals[4], gals[8])
    distance1to7 = res.find_path(gals[0], gals[6])
    distance3to6 = res.find_path(gals[2], gals[5])
    distance7to8 = res.find_path(gals[7], gals[8])
    assert distance5to9[2] == 9
    assert distance1to7[2] == 15
    assert distance3to6[2] == 17
    assert distance7to8[2] == 5

def test_solution_one():
    test_input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""
    res = DoIt(test_input)
    solution = res.solve_part_one()
    assert solution == 374

def test_galaxy_equal():
    g1 = Galaxy(1, 1,1)
    g2 = Galaxy(1, 1,1)
    assert g1 == g2

def test_galaxy_not_equal():
    g1 = Galaxy(1, 1,1)
    g2 = Galaxy(2, 1,2)
    assert g1 != g2

def test_galaxy_hash():
    gals: list[Galaxy] = []
    g1 = Galaxy(1, 1,1)
    g2 = Galaxy(1, 1,1)
    gals.append(g1)
    gals.append(g2)
    gals = set(gals)
    assert len(gals) == 1

def test_galaxy_combo_hash():
    gals: list[tuple[Galaxy, Galaxy]] = []
    g1 = Galaxy(1, 0,4)
    g2 = Galaxy(2, 1,9)
    combo1 = GalaxyCombo(g1, g2)

    g3 = Galaxy(1, 0,4)
    g4 = Galaxy(2, 1,9)
    combo2 = GalaxyCombo(g4, g3)
    gals.append(combo1)
    gals.append(combo2)
    gals = set(gals)
    assert len(gals) == 1

def test_get_combos():
    gals = []
    gals.append(Galaxy(1, 1, 1))
    gals.append(Galaxy(2, 1, 1))
    gals.append(Galaxy(3, 1, 1))
    gals.append(Galaxy(4, 1, 1))
    gals.append(Galaxy(5, 1, 1))
    gals.append(Galaxy(6, 1, 1))
    gals.append(Galaxy(7, 1, 1))
    gals.append(Galaxy(8, 1, 1))
    gals.append(Galaxy(9, 1, 1))
    test_input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""
    res = DoIt(test_input)
    gal = res.parse_input()
    combo = res.get_combos(gal, gals)
    assert len(combo) == 36

#def test_find_expansion_passes():
#    test_input = """
#...#......
#.......#..
##.........
#..........
#......#...
#.#........
#.........#
#..........
#.......#..
##...#.....
#"""
#    res = DoIt(test_input)
#    res.EXPANSION_CONSTANT = 1
#    parsed = res.parse_input()
#    galaxy, gals = res.number_galaxies(parsed)
#    #res._find_expansion_passes(res.galaxy: list[list[str]], row_number: int, col_number: int) -> tuple[int, int]: