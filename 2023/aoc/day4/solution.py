from aoc.utils.day import Day

day = Day(4, "Scratchcards")

def part_one():
    class Card:
        def __str__(self):
            s = f"Card {self.card_number}: "
            for w in self.winning_numbers:
                s += f"{w} "
            s += " | "
            for m in self.my_numbers:
                s += f"{m} "
            s += f" --> {self.total_points}"
            return s
    
        def __init__(self, line : str):
            self._line = line
            self.winning_numbers : list[int] = [] 
            self.my_numbers : list[int] = []
            self.card_number : int
            self.total_points : int = 0
    
            self.parse()
            self.analyze()
    
        def parse(self):
            card_info, numbers = self._line.split(":")
            self.card_number = int(card_info.replace("Card", "").strip())
    
            winners, my_nums = numbers.split("|")
    
            self.winning_numbers = [int(n.strip()) for n in winners.split(" ") if n.strip().isdigit()]
            self.my_numbers = [int(n.strip()) for n in my_nums.split(" ") if n.strip().isdigit()]
    
        def analyze(self):
            matches = [n for n in self.my_numbers if n in self.winning_numbers]
            self.count_points(len(matches))
    
        def count_points(self, count_matches: int):
            total = 0
            i = 0
            while True:
                if i == count_matches:
                    break 
                if i == 0:
                    total += 1
                else:
                    total *= 2
                i += 1
            self.total_points = total
    
    class ItDoesThings:
        def __str__(self):
            total_points = 0
            s = ""
            for c in self._cards:
                total_points += c.total_points
                s += f"{c}\n"
            s += f"Total points = {total_points}"
            return s
    
        def __init__(self, fileName : str):
            file = open(fileName, 'r')
            self._cards : list[Card] = []
            while True:
                line = file.readline()
                if not line:
                    break
                self._cards.append(Card(line.strip()))

        def get_total(self):
            total = 0
            for c in self._cards:
                total += c.total_points
            return total
    
    final = ItDoesThings('aoc/day4/input1.txt')
    return final.get_total()


def part_two():
    class Card:
        def __str__(self):
            s = f"Card {self.card_number}: "
            for w in self.winning_numbers:
                s += f"{w} "
            s += " | "
            for m in self.my_numbers:
                s += f"{m} "
            s += f" --> {self.replicas}"
            return s
    
        def __init__(self, line : str):
            self._line = line
            self.winning_numbers : list[int] = [] 
            self.my_numbers : list[int] = []
            self.card_number : int
            self.total_points : int = 0
            self.matches = 0
            self.replicas = 1
    
            self.parse()
            self.analyze()
    
        def parse(self):
            card_info, numbers = self._line.split(":")
            self.card_number = int(card_info.replace("Card", "").strip())
    
            winners, my_nums = numbers.split("|")
    
            self.winning_numbers = [int(n.strip()) for n in winners.split(" ") if n.strip().isdigit()]
            self.my_numbers = [int(n.strip()) for n in my_nums.split(" ") if n.strip().isdigit()]
    
        def analyze(self):
            matches = [n for n in self.my_numbers if n in self.winning_numbers]
            self.matches = len(matches)
    
    
    class ItDoesThings:
        def __str__(self):
            total_cards = 0
            s = ""
            for card_num, card in self._cards.items():
                s += f"{card}\n"
                total_cards += card.replicas
            s += f"Total Cards: {total_cards}"
            return s
    
        def __init__(self, fileName : str):
            file = open(fileName, 'r')
            self._cards : dict[int, Card] = {}
            while True:
                line = file.readline()
                if not line:
                    break
                card = Card(line.strip())
                self._cards[card.card_number] = card
            self.analyze_cards()
    
        def analyze_cards(self):
            for card_num, card in self._cards.items():
                if card.matches == 0:
                    continue
                for _ in range(card.replicas):
                    i = card_num + 1
                    while i <= card.matches + card_num:
                        self._cards[i].replicas += 1
                        i += 1
        def calculate_total(self):
            total =0
            for _, card in self._cards.items():
                total += card.replicas
            return total

    
    final = ItDoesThings('aoc/day4/input2.txt')
    return final.calculate_total()
    
