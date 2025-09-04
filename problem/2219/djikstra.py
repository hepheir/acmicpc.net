# 2219번: 보안 시스템 설치

from typing import List, Tuple
import heapq
import sys


MAX_N = 200
MAX_M = 10000
MAX_C = 10000

INF = MAX_N*MAX_M*MAX_C+1


G = [[] for _ in range(MAX_N+1)]
dist = [[INF] * (MAX_N+1) for _ in range(MAX_N+1)]


def all_pair_shortest_path(G: List[List[Tuple[int, int]]], dist: List[List[int]], N: int):
    # O(N (N+M) log M)
    heap = []
    for u in range(1, N+1):
        # O((N+M) log M): Dijkstra
        node_dist = dist[u]
        node_dist[u] = 0
        heapq.heappush(heap, (node_dist[u], u))
        while heap:
            d, u = heapq.heappop(heap)
            if d > node_dist[u]:
                continue
            for v, w in G[u]:
                if node_dist[v] > node_dist[u]+w:
                    node_dist[v] = node_dist[u]+w
                    heapq.heappush(heap, (node_dist[v], v))


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    for _ in range(M):
        A, B, C = map(int, sys.stdin.readline().split())
        G[A].append((B, C))
        G[B].append((A, C))

    all_pair_shortest_path(G, dist, N)

    answer = min(range(1, N+1), key=lambda u: sum(dist[u]))
    print(answer)
