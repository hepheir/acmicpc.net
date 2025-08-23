# 24762번: Ticket Completed?

import collections
import sys


N, M = map(int, sys.stdin.readline().split())

rank = list(range(N+1))
subset_size = collections.Counter()


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


for i in range(1, N+1):
    subset_size[find(i)] += 1

answer = sum(size * (size-1) for size in subset_size.values()) / (N * (N-1))

print(answer)
