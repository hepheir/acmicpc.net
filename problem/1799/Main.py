# 1799번: 비숍

from typing import List, Set
import sys

INV_SQRT_2 = 1/(2**0.5)


def backtracking(y_stack: List[List[int]], x_used: Set[float], max_count: int = 0) -> int:
    if not y_stack:
        return max(max_count, len(x_used))
    if len(x_used)+len(y_stack) <= max_count:
        return max_count
    row = y_stack.pop()
    max_count = max(max_count, backtracking(y_stack, x_used, max_count))
    for x in row:
        if x not in x_used:
            x_used.add(x)
            max_count = max(max_count, backtracking(y_stack, x_used, max_count))
            x_used.discard(x)
    y_stack.append(row)
    return max_count


N = int(sys.stdin.readline())
y_stacks = dict()
for y in range(N):
    for x, is_placable in enumerate(map(int, sys.stdin.readline().split())):
        rx = INV_SQRT_2*(x-y)
        ry = INV_SQRT_2*(x+y)
        if x >= N:
            continue
        if ry not in y_stacks:
            y_stacks[ry] = list()
        if is_placable:
            y_stacks[ry].append(rx)

y_stacks = [y_stacks[y] for y in sorted(y_stacks)]

answer = 0
answer += backtracking(y_stacks[0::2], set()) # 햐양 칸
answer += backtracking(y_stacks[1::2], set()) # 검은 칸
print(answer)
