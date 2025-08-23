# 24762번: Ticket Completed?

import collections
import math
import sys


N, M = map(int, sys.stdin.readline().split())
rank = list(range(N+1))


def find(i: int) -> int:
    if rank[i] != i:
        rank[i] = find(rank[i])
    return rank[i]


def union(i: int, j: int):
    i = find(i)
    j = find(j)
    if i != j:
        rank[i] = j


for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    union(i, j)


subset_size = collections.Counter()
for i in range(1, N+1):
    subset_size[find(i)] += 1

answer = 0
for size in subset_size.values():
    answer += math.comb(size, 2)
answer /= math.comb(N, 2)

print(answer)
