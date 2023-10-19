from __future__ import annotations
import dataclasses
import functools
import heapq
import sys


@dataclasses.dataclass
class Item:
    weight: int
    value: int

    def __lt__(self, other: Item) -> bool:
        return (self.value / self.weight, self.weight) < (other.value / other.weight, other.weight)


def solve():
    N, K = map(int, sys.stdin.readline().split())
    items: list[Item] = []
    for _ in range(N):
        items.append(Item(*map(int, sys.stdin.readline().split())))
    items.sort()

    @functools.cache
    def find_max_value(spare_weights: int, nth_item: int = 0) -> int:
        if nth_item == len(items) or spare_weights < 0:
            return 0
        item = items[nth_item]
        value = 0
        if spare_weights >= item.weight:
            value = item.value + find_max_value(spare_weights-item.weight, nth_item+1)
        return max(value, find_max_value(spare_weights, nth_item+1))

    print(find_max_value(K))


if __name__ == "__main__":
    solve()
