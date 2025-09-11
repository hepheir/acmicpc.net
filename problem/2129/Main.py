# 2129번: 드라이브 파이널

import heapq
import sys


INF = sys.maxsize


def solve(N: int, M: int, S: int, T: int, G: list) -> str:
    G_filtered = [[] for _ in range(N)]
    for u in range(N):
        if not G[u]:
            continue
        min_a, _, _ = min(G[u])
        for i in range(len(G[u])):
            if min_a == G[u][i][0]:
                G_filtered[u].append(G[u][i])
    G = G_filtered

    # Bellman-ford

    cost = [INF] * N
    dist = [INF] * N
    prev = [None] * N
    cost[S] = 0
    dist[S] = 0

    for _ in range(N-1):
        for u in range(N-1):
            for c, d, v in G[u]:
                if cost[v] > cost[u] + c:
                    cost[v] = cost[u] + c
                    dist[v] = dist[u] + d
                    prev[v] = u
                if dist[v] > dist[u] + d:
                    dist[v] = dist[u] + d
                    prev[v] = u

    if dist[T] == INF:
        return 'VOID'

    targets = set()
    node = T
    while node is not None:
        targets.add(node)
        node = prev[node]

    for _ in range(N-1):
        for u in range(N-1):
            for c, d, v in G[u]:
                if cost[v] > cost[u] + c:
                    cost[v] = cost[u] + c
                    dist[v] = dist[u] + d
                    if v in targets:
                        return 'UNBOUND'
                if dist[v] > dist[u] + d:
                    dist[v] = dist[u] + d
                    if v in targets:
                        return 'UNBOUND'

    return f'{cost[T]} {dist[T]}'


if __name__ == '__main__':
    N, M, S, T = map(int, sys.stdin.readline().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v, a, c, b = map(int, sys.stdin.readline().split())
        G[u].append((a, c, v))
        G[v].append((b, c, u))
    answer = solve(N, M, S, T, G)
    print(answer)
