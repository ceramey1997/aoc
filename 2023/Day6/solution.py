class Outcome:
    def __str__(self):
        return f"Button Time: {self.button_time} -- Distance: {self.distance}"

    def __init__(self, distance: int, button_time: int):
        self.button_time = button_time
        self.distance = distance 

class Race:
    def __str__(self):
        if self.part == 1:
            s = ""
            for w_oc in self.winning_outcomes:
                s += f"{w_oc}\n"
            return s
        return ""

    def __init__(self, time: int, record_distance:int, part2: bool = False):
        self.part = 1
        if part2:
            self.part = 2
        self.time = time
        self.record_distance = record_distance
        self.outcomes = self.find_outcomes()
        self.winning_outcomes : list[Outcome] = []
        for oc in self.outcomes:
            if oc.distance > self.record_distance:
                self.winning_outcomes.append(oc)

    def find_outcomes(self):
        distance_outcomes : list[Outcome] = []
        for milliseconds in range(self.time + 1):
            moving_time = self.time - milliseconds
            millimeters_per_millisecond = milliseconds
            d = moving_time * millimeters_per_millisecond 
            distance_outcomes.append(Outcome(d, milliseconds))
        return distance_outcomes

class ItDoesThings:
    def __str__(self):
        if self.part == 1:
            total = 1
            s = ""
            for r in self.races:
                total *= len(r.winning_outcomes)
                s += f"{r}\n"
            s += f"Margin Of Error: {total}"
            return s
        else:
            return f"{len(self.race.winning_outcomes)}"

    def __init__(self, fileName : str):
        self.fileName = fileName
        self.part = 1

    def part1(self):
        self.races : list[Race] = []
        file = open(self.fileName, 'r')
        times, distances = file.read().strip().split("\n")
        times = list(map(int, times.split(":")[1].strip().split()))
        distances = list(map(int, distances.split(":")[1].strip().split()))

        for t, d in zip(times, distances):
            race = Race(t, d)
            self.races.append(race)

    def part2(self):
        self.part = 2
        self.race: Race
        file = open(self.fileName, 'r')
        
        time, distance = file.read().strip().split("\n")
        time = int("".join(list(time.split(":")[1].strip().split())))
        distance = int("".join(list(distance.split(":")[1].strip().split())))

        self.race = Race(time, distance, True)


final = ItDoesThings('input2.txt')
final.part2()
print(final)
