# 2219번: 보안 시스템 설치

from typing import List, Tuple
import sys


MAX_N = 200
MAX_M = 10000
MAX_C = 10000

INF = MAX_N*MAX_M*MAX_C+1


G = [[] for _ in range(MAX_N+1)]
dist = [[INF] * (MAX_N+1) for _ in range(MAX_N+1)]


def all_pair_shortest_path(G: List[List[Tuple[int, int]]], dist: List[List[int]], N: int):
    # O(N^3+M)
    # O(N+M)
    for u in range(1, N+1):
        dist[u][u] = 0
        for v, w in G[u]:
            dist[u][v] = w
    # O(N^3): Floyd-Warshall algorithm
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if dist[i][j] > dist[i][k]+dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    for _ in range(M):
        A, B, C = map(int, sys.stdin.readline().split())
        G[A].append((B, C))
        G[B].append((A, C))

    all_pair_shortest_path(G, dist, N)

    answer = min(range(1, N+1), key=lambda u: sum(dist[u]))
    print(answer)
