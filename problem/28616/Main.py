# 28616번: Биомаркеры

import dataclasses
import sys
import typing

MAX_K = int(5e5)


def main():
    K = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    answer = solve(K, S)
    print(answer)


@dataclasses.dataclass
class Node:
    value: str
    size: int = 0
    rem: int = 0
    prev: typing.Optional['Node'] = None

    def __init__(self, value: str):
        self.value = value
        if value == '*':
            self.size = 0
            self.rem = 0
            self.prev = None
        else:
            self.size = 1
            self.rem = int(value) % 3
            self.prev = None

    def __lt__(self, other: 'Node') -> bool:
        if self.size < other.size:
            return True
        if self.size > other.size:
            return False
        self_node = self
        other_node = other
        while self_node is not None and other_node is not None:
            if self_node == other_node:
                # 비교가 무의미함.
                return False
            if self_node.value < other_node.value:
                return True
            if self_node.value > other_node.value:
                return False
            self_node = self_node.prev
            other_node = other_node.prev
        return False

    def __str__(self) -> str:
        node = self
        values = []
        while node is not None:
            values.append(node.value)
            node = node.prev
        return ''.join(values)

    def __repr__(self) -> str:
        return self.__str__()

    def concat_left(self, value: str) -> 'Node':
        if self.value == '*':
            return Node(value=value)
        node = Node(value=value)
        node.size = node.size + self.size
        node.rem = (node.rem + self.rem) % 3
        node.prev = self
        return node


def solve(K: int, S: str) -> str:
    dp_prev: typing.List[Node] = [Node(value='*')] * 3
    dp_curr: typing.List[Node] = [Node(value='*')] * 3
    for i in reversed(range(K)):
        dp_prev, dp_curr = dp_curr, dp_prev
        for r in range(3):
            dp_curr[r] = dp_prev[r]
        node = Node(S[i])
        if dp_curr[node.rem] < node:
            dp_curr[node.rem] = node
        for r in range(3):
            node = dp_prev[r].concat_left(S[i])
            if dp_curr[node.rem] < node:
                dp_curr[node.rem] = node
    answer = dp_curr[0].__str__()
    if answer == '*':
        return '0'
    return str(int(answer))


if __name__ == '__main__':
    main()
