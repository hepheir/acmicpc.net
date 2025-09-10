# 1184번: 귀농

import collections
import sys


N = int(sys.stdin.readline())
A = [[0] * (N+1) for _ in range(N+1)]
prefix_sum = [[0] * (N+1) for _ in range(N+1)]

upper_r = collections.defaultdict(collections.Counter)
upper_l = collections.defaultdict(collections.Counter)


def range_sum(i_lo: int, j_lo: int, i_hi: int, j_hi: int) -> int:
    return (
        + prefix_sum[i_hi][j_hi]
        - prefix_sum[i_lo-1][j_hi]
        - prefix_sum[i_hi][j_lo-1]
        + prefix_sum[i_lo-1][j_lo-1]
    )


for i in range(N):
    for j, cost in enumerate(map(int, sys.stdin.readline().split())):
        A[i][j] = cost
        prefix_sum[i][j] = (
            + A[i][j]
            + prefix_sum[i-1][j]
            + prefix_sum[i][j-1]
            - prefix_sum[i-1][j-1]
        )
        for i_lo in range(i+1):
            for j_lo in range(j+1):
                a = range_sum(i_lo, j_lo, i, j)
                upper_l[i_lo, j][a] += 1
                upper_r[i, j][a] += 1


answer = 0
for i_lo in range(N):
    for j_lo in range(N):
        for i_hi in range(i_lo, N):
            for j_hi in range(j_lo, N):
                a = range_sum(i_lo, j_lo, i_hi, j_hi)
                answer += upper_r[i_lo-1, j_lo-1][a] + upper_l[i_hi+1, j_lo-1][a]

print(answer)
