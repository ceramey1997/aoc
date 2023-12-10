from enum import Enum

class Direction(Enum):
    LEFT = 0
    RIGHT = 1

class Node:
    def __str__(self):
        return f"{self.key} = ({self.left}, {self.right})"

    def __init__(self, network: str):
        key, left, right = self.parse_network(network)
        self.key = key
        self.left = left
        self.right = right

    def parse_network(self, network: str) -> tuple[str, str, str]:
        key, left_right = network.split("=")
        left, right = left_right.replace("(", "").replace(")", "").strip().split(",")
        return key.strip(), left.strip(), right.strip()

    def next_node(self, dir : Direction) -> str:
        match dir:
            case Direction.RIGHT:
                return self.right
            case Direction.LEFT:
                return self.left
            case _:
                raise Exception("bad direction provided!")

class DoingIt:
    def __str__(self):
        return f"Steps: {self.steps}"

    def __init__(self, fileName: str):
        file = open(fileName, 'r')
        [*instructions], _, *network = file.read().strip().split("\n")
        network: list[str] = [n.strip() for n in network]
        self.nodes: list[Node] = [Node(n) for n in network]
        self.instructions = [Direction.RIGHT if i == "R" else Direction.LEFT  for i in instructions]
        self.steps = 0
        idx = 0
        next_node = list(filter(lambda n: n.key == "AAA", self.nodes))[0]
        while True:
            if next_node.key == "ZZZ":
                break
            node = list(filter(lambda n: n.key == next_node.key, self.nodes))[0]
            next_key = node.next_node(self.instructions[idx])
            next_node = self.get_next_node(next_key)
            idx += 1
            if idx == len(self.instructions):
                idx = 0
            self.steps += 1

    def get_next_node(self, key: str) -> Node:
        return list(filter(lambda n: n.key == key, self.nodes))[0]


final = DoingIt("input1.txt")
print(final)
