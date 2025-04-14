import functools
import sys


MAX_N = 100
MAX_T = 10000
INF = MAX_N * MAX_T * 10

sys.setrecursionlimit(10*MAX_N*MAX_T*MAX_N)


N, A, B = map(int, sys.stdin.readline().split())
T = sorted(map(int, sys.stdin.readline().split()))


@functools.lru_cache(maxsize=MAX_N*MAX_T*MAX_N)
def solve(i: int = 0, time: int = 0, cost: int = A) -> int:
    if i == N:
        return 0
    max_count = 0
    if cost == A:
        for X in range(1, A):
            max_count = max(max_count, solve(i, time+B*X, A-X))
    if time+cost > T[i]:
        max_count = max(max_count, solve(i+1, time, cost))
    else:
        max_count = max(max_count, solve(i+1, time+cost, cost) + 1)
    return max_count


print(solve())
