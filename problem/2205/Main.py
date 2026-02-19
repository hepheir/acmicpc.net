# 2205번: 저울 추 만들기

import sys

MAX_N = 10000

sys.setrecursionlimit(10*MAX_N)

n = int(sys.stdin.readline())

is_used = [False] * (n+1)
stack = []


def get_possible_y(x: int):
    sum_value = 2
    while (sum_value << 1) <= (n+x):
        sum_value <<= 1
    while sum_value > x:
        yield sum_value - x
        sum_value >>= 1


def construct(x: int) -> bool:
    if x > n:
        return True
    for y in get_possible_y(x):
        if is_used[y]:
            continue
        is_used[y] = True
        stack.append(y)
        if construct(x+1):
            return True
        stack.pop()
        is_used[y] = False
    return False

assert construct(1)

print(*stack, sep='\n')
