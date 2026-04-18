# 31929번: 너 재능 있어

import functools
import sys

MAX_N = 1000
MAX_M = 1000

sys.setrecursionlimit(10 * (MAX_N + MAX_M))


N = int(sys.stdin.readline())
W = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())

INF = sum(W) + sum(L) + 1


@functools.cache
def solve(i: int, j: int) -> int:
    if i == 0 and j == 0:
        return 0

    max_score = -INF

    # Win
    if i > 0:
        max_score = max(max_score, solve(i-1, j) + W[i-1])

    # Lose
    if j > 0:
        score = solve(i, j-1)
        b = (score % K) if (score % K != 0) else sys.maxsize
        max_score = max(max_score, score - min(L[j-1], b))

    return max_score


print(solve(N, M))
