# 1799번: 비숍

from collections import defaultdict
from typing import *
import sys


SQRT_2 = 2**0.5
INV_SQRT_2 = 1/SQRT_2


N = int(sys.stdin.readline())
grid = defaultdict(list)
for y in range(N):
    for x, is_placable in enumerate(map(int, sys.stdin.readline().split())):
        if is_placable:
            grid[INV_SQRT_2*(x+y)].append(INV_SQRT_2*(x-y))


y_stack: List[float] = list(grid.keys())
x_used: Set[float] = set()

answer = 0


def backtracking():
    global answer
    if not y_stack:
        answer = max(answer, len(x_used))
        return
    if len(x_used)+len(y_stack) <= answer:
        return
    y = y_stack.pop()
    backtracking()
    for x in grid[y]:
        if x not in x_used:
            x_used.add(x)
            backtracking()
            x_used.discard(x)
    y_stack.append(y)


backtracking()
print(answer)
