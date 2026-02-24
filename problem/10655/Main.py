# 10655번: 마라톤 1

import sys

MAX_N = 100000

x = [0] * MAX_N
y = [0] * MAX_N


def get_dist_between(i: int, j: int) -> float:
    return abs(x[i] - x[j]) + abs(y[i] - y[j])


N = int(sys.stdin.readline())
for i in range(N):
    x[i], y[i] = map(int, sys.stdin.readline().split())

answer = float('inf')
dist_sum = sum(get_dist_between(i, i+1) for i in range(N-1))
for i in range(1, N-1):
    answer = min(answer,
                 dist_sum
                 - get_dist_between(i-1, i)
                 - get_dist_between(i, i+1)
                 + get_dist_between(i-1, i+1))

print(answer)
