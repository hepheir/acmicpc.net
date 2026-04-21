# 11060번: 점프 점프

import functools
import sys

MAX_N = 1000
INF = MAX_N + 1

sys.setrecursionlimit(10 * MAX_N)


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))


@functools.cache
def solve(i: int) -> int:
    if i >= N-1:
        return 0
    if A[i] == 0:
        return INF
    return min(solve(i+a) for a in range(1, A[i]+1)) + 1


if solve(0) >= INF:
    print(-1)
else:
    print(solve(0))
