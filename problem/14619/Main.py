# 14619번: 섬 여행

from functools import cache
from typing import Set
import sys

INF = sys.maxsize
MAX_K = 500

N, M = map(int, sys.stdin.readline().split())
H = [None, *map(int, sys.stdin.readline().split())]

G = [[] for _ in range(N+1)]
for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    G[X].append(Y)
    G[Y].append(X)


def solve(A: int, K: int) -> int:
    answer = INF
    for node in visitable_nodes(A, K):
        if answer > H[node]:
            answer = H[node]
    if answer == INF:
        return -1
    return answer



@cache
def visitable_nodes(node: int, steps: int) -> Set[int]:
    answer = set()
    if steps == 0:
        answer.add(node)
    else:
        for neighbor in G[node]:
            answer.update(visitable_nodes(neighbor, steps-1))
    return answer


T = int(sys.stdin.readline())
for _ in range(T):
    A, K = map(int, sys.stdin.readline().split())
    sys.stdout.write(f'{solve(A, K)}\n')
