# 9657번: 돌 게임 3

import sys
from functools import cache

MAX_N = 1000
sys.setrecursionlimit(10*MAX_N)


@cache
def solve(n: int) -> bool:
    for x in (1, 3, 4):
        if n == x:
            return True
        if n > x and not solve(n-x):
            return True
    return False


N = int(input())
print('SK' if solve(N) else 'CY')
