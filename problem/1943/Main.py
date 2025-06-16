from typing import *
from functools import cache
import sys


COIN: List[Tuple[int, int]] = [] # [(unit, count), ...]


@cache
def knapsack(i: int, capacity: int) -> bool:
    if capacity < 0:
        return False
    if i == len(COIN):
        return capacity == 0
    unit, max_count = COIN[i]
    for count in reversed(range(min(max_count, capacity//unit)+1)):
        if knapsack(i+1, capacity-unit*count):
            return True
    return False


for _ in range(3):
    knapsack.cache_clear()
    COIN.clear()
    N = int(sys.stdin.readline())
    total_balance = 0
    for i in range(N):
        unit, count = map(int, sys.stdin.readline().split())
        total_balance += unit * count
        COIN.append((unit, count))
    COIN.sort(reverse=True)
    if (total_balance % 2 == 0) and knapsack(0, total_balance//2):
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
