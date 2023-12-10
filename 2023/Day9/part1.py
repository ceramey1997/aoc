from concurrent.futures import ThreadPoolExecutor, Future, as_completed

class DoingIt:
    def __str__(self):
        return f"{self.total}"

    def __init__(self, fileName: str):
        file = open(fileName, 'r')
        self.histories = [[int(i) for i in l.split()] for l in file.read().strip().split("\n")]
        self.traverse_history(self.histories[0])

        self.extrapolated_data : list[list[list[int]]]
        with ThreadPoolExecutor() as exec:
            results : list[Future[list[list[int]]]] = [exec.submit(self.traverse_history, h) for h in self.histories]
            self.extrapolated_data = [self.extrapolate(r.result()) for r in as_completed(results)]
        
        self.total: int = sum([e[0][-1] for e in self.extrapolated_data])


    def extrapolate(self, full_hist: list[list[int]]) -> list[list[int]]:
        full_hist.reverse()
        for idx, his in enumerate(full_hist):
            if idx == len(full_hist) - 1:
                break
            if idx == 0:
                his.append(0)
                continue
            amount_to_increase = his[-1]
            adding_to = full_hist[idx+1][-1]
            extrapolated_data_point = adding_to + amount_to_increase
            full_hist[idx+1].append(extrapolated_data_point)
        full_hist.reverse()
        return full_hist

    def traverse_history(self, hist: list[int]) -> list[list[int]]:
        full_history = [hist]
        def rec(single_hist: list[int]):
            diffs = []
            for idx, data_point in enumerate(single_hist):
                if idx == len(single_hist) - 1:
                    break
                d = single_hist[idx+1] - data_point 
                diffs.append(d)
            full_history.append(diffs)
            if len([d for d in diffs if d == 0]) == len(diffs):
                return
            else:
                rec(diffs)
        rec(hist)
        return full_history


final = DoingIt("input1.txt")
print(final)
