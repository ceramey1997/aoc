from typing import List

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

class FindItAll:

    def __str__(self):
        #for game in self._impossibles:
        #    print(game)
        #for game in self._possibles:
        #    print(game)
        pos_ints = [g.num for g in self._possibles]
        #impos_ints = [g.num for g in self._impossibles]
        #print(f"Impossibles\n {impos_ints}")
        #print(f"Possibles\n {pos_ints}")

        tot = 0
        for g in pos_ints:
            tot = tot + g
        return str(tot)


    def __init__(self):
        self._games: List[Game] = []
        self._impossibles : List[Game] =[] 
        self._possibles: List[Game] = []
        self._bag = {
            "red": 12,
            "green": 13,
            "blue": 14
        }
        file = open('input1.txt', 'r')
        while True:
            line = file.readline()
            if not line:
                break
            game = Game()
            game.parse(line)
            self._games.append(game)
        for g in self._games:
            possible = self.is_game_possible(g)
            if possible:
                self._possibles.append(g)
                continue
            self._impossibles.append(g)



    def is_game_possible(self, game: Game) -> bool:
        for pull in game.pulls:
            possible = self.pull_possible(pull)
            if not possible:
                return False
        return True

    def pull_possible(self, pull: Pull) -> bool:
        totals = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for c in pull.colors:
            totals[c.color] += c.amount

        if totals["red"] > self._bag["red"]:
            return False
        if totals["green"] > self._bag["green"]:
            return False
        if totals["blue"] > self._bag["blue"]:
            return False
        return True


g = FindItAll()
print(g)
