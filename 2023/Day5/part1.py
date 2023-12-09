class ItDoesThings:
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

final = ItDoesThings('input1.txt')
print(final)
