from typing import List

class Total:
    def __init__(self):
        self.red = 0
        self.blue = 0
        self.green = 0

    def __str__(self):
        return f"red: {self.red}, green: {self.green}, blue: {self.blue}"

    def add(self, color: str, amount: int) -> None:
        if color == "red":
            self.red += amount
            return
        if color == "green":
            self.green += amount
            return
        if color == "blue":
            self.blue += amount
            return

class Color:
    def __init__(self):
        self.color : str
        self.amount : int

    def __str__(self):
        return f"{self.amount} {self.color}"

    def parse(self, partial_line : str):
        partial_line = partial_line.strip()
        num, color = partial_line.split(" ")
        self.amount = int(num.strip())
        self.color = color.strip()

class Pull:

    def __init__(self):
        self.colors: List[Color]

    def __str__(self):
        ret = ""
        for i in range(len(self.colors)):
            ret += f"{self.colors[i]}"
            if not i == len(self.colors) - 1:
                ret += ", "
        return ret

    def parse(self, partial_line: str):
        split_colors = partial_line.split(",")
        self.colors = []
        for c in split_colors:
            single_color = Color()
            single_color.parse(c)
            self.colors.append(single_color)

class Game:
    def __init__(self):
        self.num:int
        self.pulls : List[Pull] = []

    def __str__(self):
        ret = f"Game {self.num}: "
        for i in range(len(self.pulls)):
            ret += f"{self.pulls[i]}"
            if not i == len(self.pulls) - 1:
                ret += "; "
        return ret

    def parse(self, line: str):
        game, pulls_unparsed = line.split(":")
        self.num = int(game.split(" ")[1])
        split_pulls = pulls_unparsed.split(';')
        for p in split_pulls:
            single_pull = Pull()
            single_pull.parse(p.strip())
            self.pulls.append(single_pull)

class GameInfo:
    def __str__(self):
        s = f"{self.game} --> {self.minimum}"
        return s

    def __init__(self, game : Game, min_totals : Total):
        self.game : Game = game
        self.minimum : Total = min_totals
        self.power = 0
    def find_power(self) -> int:
        self.power = self.minimum.red * self.minimum.green * self.minimum.blue
        return self.power

class FindItAll:

    def __str__(self):
        t = ""
        total = 0
        for gi in self._gInfo:
            t += f"{gi}"
            power = gi.find_power()
            total += gi.power
            t += f" **POWER: {power}**\n"



        t += f"\n\nTOTAL == > {total}"
        return t

    def __init__(self):
        self._games: List[Game] = []
        self._gInfo : List[GameInfo] = []

        file = open('input2.txt', 'r')
        while True:
            line = file.readline()
            if not line:
                break
            game = Game()
            game.parse(line)
            self._games.append(game)
        for g in self._games:
            gm = self.get_game_minimum(g)
            game_info = GameInfo(g, gm)
            game_info.minimum = gm
            self._gInfo.append(game_info)

    def get_game_minimum(self, game: Game) -> Total:
        tots : List[Total] = []
        for pull in game.pulls:
            tot = self.pull_color_needs(pull)
            tots.append(tot)

        return self.find_minimum(tots)

    def find_minimum(self, tots: List[Total]) -> Total:
        final_minimum = Total()
        for t in tots:
            if t.blue > final_minimum.blue:
                final_minimum.blue = t.blue
            if t.green > final_minimum.green:
                final_minimum.green = t.green
            if t.red > final_minimum.red:
                final_minimum.red = t.red
        return final_minimum 


    def pull_color_needs(self, pull: Pull) -> Total:
        tot = Total()
        for c in pull.colors:
            tot.add(c.color, c.amount)
        return tot

g = FindItAll()
print(g)
