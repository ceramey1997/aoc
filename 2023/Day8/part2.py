from enum import Enum
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import Future
from math import lcm
import time

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
        return f"{self.steps}"

    def __init__(self, fileName: str):
        file = open(fileName, 'r')
        [*instructions], _, *network = file.read().strip().split("\n")
        network: list[str] = [n.strip() for n in network]
        self.nodes: list[Node] = [Node(n) for n in network]
        self.instructions = [Direction.RIGHT if i == "R" else Direction.LEFT  for i in instructions]
        next_nodes: list[Node] = list(filter(lambda n: n.key.endswith("A"), self.nodes))
        res : list[int] = []
        with ThreadPoolExecutor() as executor:
            results: list[Future[int]] = [executor.submit(self.traverse, n) for n in next_nodes]
            for r in results:
                res.append(r.result())
        self.steps = lcm(*res)

    def traverse(self, node: Node) -> int:
        steps = 0
        idx = 0
        while True:
            if node.key.endswith("Z"):
                return steps
            direction = self.instructions[idx]
            next_key : str = node.next_node(direction)
            node = self.get_next_node(next_key)
            idx += 1
            if idx == len(self.instructions):
                idx = 0
            steps += 1

    def get_next_node(self, key: str) -> Node:
        return list(filter(lambda n: n.key == key, self.nodes))[0]

start = time.perf_counter()
final = DoingIt("input2.txt")
finish = time.perf_counter()
print(final)
print(f"Run Time: {round(finish-start, 2)} (s)")
