from typing import List

class Color:
    color: str
    amount: int

    def parse(self, partial_line : str):
        partial_line = partial_line.strip()
        num, color = partial_line.split(" ")
        self.amount = int(num.strip())
        self.color = color.strip()

class Pull:
    colors: List[Color]

    def parse(self, partial_line: str):
        split_colors = partial_line.split(",")
        self.colors = []
        for c in split_colors:
            single_color = Color()
            single_color.parse(c)
            self.colors.append(single_color)

class Series:
    pulls: List[Pull]

    def parse(self, partial_line: str):
        split_pulls = partial_line.split(";")
        self.pulls = []
        for p in split_pulls:
            single_pull = Pull()
            single_pull.parse(p.strip())
            self.pulls.append(single_pull)

class Game:
    num:int
    series : Series
    def parse(self, line: str):
        game, series_unparsed = line.split(":")
        self.num = int(game.split(" ")[1])
        self.series = Series()
        self.series.parse(series_unparsed)

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

file = open('input1.txt', 'r')
games :List[Game] = []
while True:
    line = file.readline()
    if not line:
        break
    game = Game()
    game.parse(line)
    games.append(game)

import pdb;
totals = {
    "red": 0,
    "green": 0,
    "blue": 0
}

impossibles : list[int] = []
possibles: list[int] = []

print_game_possibles :List[str]= []

for g in games:
    game_print = f"{g.num}: "
    for p in g.series.pulls:
        for c in p.colors:
            totals[c.color]+= c.amount
            game_print += f"{c.amount} {c.color}, "
        game_print +="; "
        pdb.set_trace()
    if totals["red"] > bag["red"]:
        impossibles.append(g.num)

        totals = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        #print(f"{g.num} -> false b/c red")
        #print(totals["red"])
        game_print = ""
        continue
    if totals["green"] > bag["green"]:
        impossibles.append(g.num)
        #print(f"{g.num} -> false b/c green")
        totals = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        game_print = ""
        continue
    if totals["blue"] > bag["blue"]:
        impossibles.append(g.num)
        totals = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        #print(f"{g.num} -> false b/c blue")
        game_print = ""
        continue

    print_game_possibles.append(game_print)
    game_print = ""
    possibles.append(g.num)
    #print(totals)
    totals = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    #print(totals)

print(possibles)
for pp in print_game_possibles:
    print(pp)
totals = 0
for p in possibles:
    totals += p
print(impossibles)
print(totals)
