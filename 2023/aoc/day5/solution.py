from aoc.utils.day import Day

day = Day(5, "If You Give A Seed A Fertilizer")

class Part1_DoIt:
    def __str__(self):
        return f"{min(self.seeds)}"

    def __init__(self, fileName : str):
        file = open(fileName, 'r')
        input_seeds, *blocks = file.read().split("\n\n")
        self.seeds = list(map(int,input_seeds.split(":")[1].split()))

        for block in blocks:
            ranges = []
            for line in block.splitlines()[1:]:
                dest_range_start, source_range_start, range_length = map(int, line.split())
                ranges.append([dest_range_start, source_range_start, range_length])
            news = []
            for seed in self.seeds:
                for dest_range_start, source_range_start, range_length in ranges:
                    if seed in range(source_range_start, source_range_start + range_length):
                        new_val = seed - source_range_start + dest_range_start
                        news.append(new_val)
                        break
                else:
                    news.append(seed)
            self.seeds = news


class Part2_DoIt:
    def __str__(self):
        return f"{min(self.seeds)[0]}"

    def __init__(self, fileName : str):
        file = open(fileName, 'r')
        input_seeds, *blocks = file.read().split("\n\n")
        inputs = list(map(int, input_seeds.split(":")[1].split()))

        self.seeds : list[tuple[int, int]] = []

        for i in range(0, len(inputs), 2):
            self.seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

        for block in blocks:
            ranges = []
            for line in block.splitlines()[1:]:
                dest_range_start, source_range_start, range_length = map(int, line.split())
                ranges.append([dest_range_start, source_range_start, range_length])
            news = []
            while len(self.seeds) > 0:
                start, end = self.seeds.pop()
                for dest_range_start, source_range_start, range_length in ranges:
                    overlap_start = max(start, source_range_start)
                    overlap_end = min(end, source_range_start + range_length)
                    if overlap_start < overlap_end:
                        news.append((overlap_start - source_range_start + dest_range_start, overlap_end - source_range_start + dest_range_start))
                        if overlap_start > start:
                            self.seeds.append((start, overlap_start))
                        if end > overlap_end:
                            self.seeds.append((overlap_end, end))
                        break
                else:
                    news.append((start, end))

            self.seeds = news

def part_one():
    final = Part1_DoIt('aoc/day5/input1.txt')
    return min(final.seeds)

def part_two():
    final = Part2_DoIt('aoc/day5/input2.txt')
    return min(final.seeds)[0]

