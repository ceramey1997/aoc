from enum import Enum 
from functools import cmp_to_key

class Combination(Enum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIRS = 2
    THREE_KIND = 3
    FULL_HOUSE = 4
    FOUR_KIND = 5
    FIVE_KIND = 6

class Card(Enum):
    JOKER = 0
    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    SEVEN = 6
    EIGHT = 7
    NINE = 8
    TEN = 9
    QUEEN = 10
    KING = 11
    ACE = 12

class Hand:
    def __str__(self):
        return f"({self.rank}) {''.join(self.hand)}-{''.join(self.updated_hand)} - {self.hand_type} - BID:{self.bid} - WINNINGS:{self.winnings}"

    def __init__(self, line: str):
        self.parse_line(line)
        self.kind : Combination
        self.rank = 0
        self.winnings = 0

    def parse_line(self, line: str) -> None:
        hand, bid = line.split(" ")
        self.bid: int = int(bid)
        hand = [*hand]
        self.hand : list[str] = hand
        self.enum_hand : list[Card] = self.build_enum_hand()
        self.updated_hand : list[str] = []
        self.hand_type : Combination | None = None
        self.card1 : Card = self.card_to_enum(hand[0])
        self.card2 : Card = self.card_to_enum(hand[1])
        self.card3 : Card = self.card_to_enum(hand[2])
        self.card4 : Card = self.card_to_enum(hand[3])
        self.card5 : Card = self.card_to_enum(hand[4])
        self.determine_type()

    def build_enum_hand(self) -> list[Card]:
        h = []
        for c in self.hand:
            h.append(self.card_to_enum(c))
        return h

    def card_to_enum(self, str_card : str) -> Card:
        if str_card == "2":
            return Card.TWO
        elif str_card == "3":
            return Card.THREE
        elif str_card == "4":
            return Card.FOUR
        elif str_card == "5":
            return Card.FIVE
        elif str_card == "6":
            return Card.SIX
        elif str_card == "7":
            return Card.SEVEN
        elif str_card == "8":
            return Card.EIGHT
        elif str_card == "9":
            return Card.NINE
        elif str_card == "T":
            return Card.TEN
        elif str_card == "J":
            return Card.JOKER
        elif str_card == "Q":
            return Card.QUEEN
        elif str_card == "K":
            return Card.KING
        elif str_card == "A":
            return Card.ACE
        else:
            raise Exception(f"unknown card given {str_card}")

    def determine_type2(self):
        pass

    def determine_type(self):
        card_value : dict[str, int] = {i:self.hand.count(i) for i in self.hand}
        enum_card_value : dict[Card, int] = {i:self.enum_hand.count(i) for i in self.enum_hand}
        counts = card_value.values()
        count_jokers : int = len([c for c in self.enum_hand if c == Card.JOKER]) 
        if count_jokers == 5:
            self.hand_type = Combination.FIVE_KIND
        elif count_jokers == 4:
            self.hand_type = Combination.FIVE_KIND
        elif count_jokers == 3:
            t = self.determine_one_two_from3(enum_card_value)
            if t != None:
                self.hand_type = t

        elif count_jokers == 2:
            t = self.determine_one_two_three_from2(enum_card_value)
            if t != None:
                self.hand_type = t

        elif count_jokers == 1:
            t = self.determine_one_two_three_from1(enum_card_value)
            if t != None:
                self.hand_type = t

        if self.hand_type == None:
            if 5 in counts:
                self.hand_type = Combination.FIVE_KIND
            elif 4 in counts:
                self.hand_type = Combination.FOUR_KIND
            elif 3 in counts:
                if 2 in counts:
                    self.hand_type = Combination.FULL_HOUSE
                else:
                    self.hand_type = Combination.THREE_KIND
            elif 2 in counts:
                pairs = [card for card, count in card_value.items() if count == 2]
                if len(pairs) == 2:
                    self.hand_type = Combination.TWO_PAIRS
                else:
                    self.hand_type = Combination.PAIR
            else:
                self.hand_type = Combination.HIGH_CARD

    def determine_one_two_three_from2(self, enum_card_value : dict[Card, int]) -> Combination | None:
        #try:
        #    three_card_type =list(enum_card_value.keys())[list(enum_card_value.values()).index(3)]
        #    if three_card_type == Card.JOKER:
        #        has_three = Flase
        #except:
        #    has_three = False
        try:
            two_card_type = list(enum_card_value.keys())[list(enum_card_value.values()).index(2)]
            if two_card_type == Card.JOKER:
                has_two = False
            else:
                has_two = True
        except:
            has_two = False
        if has_two:
            return Combination.FOUR_KIND
        #------------------------------------------

        try:
            list(enum_card_value.keys())[list(enum_card_value.values()).index(3)]
            has_three = True
        except:
            has_three = False
        if has_three:
            return Combination.FIVE_KIND
            #return Combination.FULL_HOUSE
        #------------------------------------------

        try:
            list(enum_card_value.keys())[list(enum_card_value.values()).index(1)]
            has_one = True
        except:
            has_one = False
        if has_one:
            return Combination.THREE_KIND
        #------------------------------------------

        return None

    def determine_one_two_three_from1(self, enum_card_value : dict[Card, int]) -> Combination | None:
        try:
            list(enum_card_value.keys())[list(enum_card_value.values()).index(4)]
            has_four = True
        except:
            has_four = False
        if has_four:
            return Combination.FIVE_KIND
        #------------------------------------------

        try:
            list(enum_card_value.keys())[list(enum_card_value.values()).index(3)]
            has_three = True
        except:
            has_three = False
        if has_three:
            return Combination.FOUR_KIND
        #------------------------------------------

        twos = []
        has_two = False
        has_two_twos = False
        for k, v in enum_card_value.items():
            if v == 2:
                twos.append(k)
        if len(twos) >= 1:
            has_two = True
        if len(twos) == 2:
            print(twos)
            has_two_twos = True
        if has_two:
            if has_two_twos:
                return Combination.FULL_HOUSE
            return Combination.THREE_KIND
        #------------------------------------------

#         try:
#             list(enum_card_value.keys())[list(enum_card_value.values()).index(3)]
#             has_three = True
#         except:
#             has_three = False
#         if has_three:
#             return Combination.FOUR_KIND
        #------------------------------------------

        ones = []
        for k, v in enum_card_value.items():
            if v == 1:
                ones.append(k)
        if len(ones) == 1 and ones[0] == Card.JOKER:
            has_one = False
        elif len(ones) > 1:
            has_one = True
        else:
            has_one = False
        if has_one:
            return Combination.PAIR
        #------------------------------------------

        return None


    def determine_one_two_from3(self, enum_card_value : dict[Card, int]) -> Combination | None:
        try:
            list(enum_card_value.keys())[list(enum_card_value.values()).index(2)]
            has_two = True
        except:
            has_two = False
        if has_two:
            self.hand_type = Combination.FIVE_KIND
        #------------------------------------------

        try:
            list(enum_card_value.keys())[list(enum_card_value.values()).index(1)]
            has_one = True
        except:
            has_one = False
        if has_one:
            self.hand_type = Combination.FOUR_KIND

    def set_rank(self, rank : int) -> None:
        self.rank = rank
        self.winnings = self.rank * self.bid

class ItDoesThings:
    def __str__(self):
        s = ""
        total = 0
        for h in self.hands:
            total += h.winnings
            s += f"{h}\n"
        s += f"Total Winnings: {total}"
        return s

    def __init__(self, fileName : str):
        self.fileName = fileName
        self.hands: list[Hand] = []
        file = open(self.fileName, 'r')
        line = file.read().strip().split("\n")
        for h in line:
            self.hands.append(Hand(h))

        self.hands.sort(key=cmp_to_key(self.sort_method))
        for i, h in enumerate(self.hands):
            h.set_rank(i + 1)


    def sort_method(self, hand1 : Hand, hand2 : Hand) -> int:
        if hand1.hand_type == None or hand2.hand_type == None:
            raise Exception("must have handtype set")
        if hand1.hand_type.value < hand2.hand_type.value:
            return -1
        elif hand1.hand_type.value > hand2.hand_type.value:
            return 1
        elif hand1.hand_type == hand2.hand_type:
            card1_sort = self.sort_card(hand1.card1.value, hand2.card1.value)
            if card1_sort != 0:
                return card1_sort
            card2_sort = self.sort_card(hand1.card2.value, hand2.card2.value)
            if card2_sort != 0:
                return card2_sort
            card3_sort = self.sort_card(hand1.card3.value, hand2.card3.value)
            if card3_sort != 0:
                return card3_sort
            card4_sort = self.sort_card(hand1.card4.value, hand2.card4.value)
            if card4_sort != 0:
                return card4_sort
            card5_sort = self.sort_card(hand1.card5.value, hand2.card5.value)
            if card5_sort != 0:
                return card5_sort
        else:
            return 0
        return 0

    def sort_card(self, card1: int, card2: int) -> int:
        if card1 < card2:
            return -1
        elif card1 > card2:
            return 1
        else:
            return 0


final = ItDoesThings("exm.txt")
print(final)
