# 2129번: 드라이브 파이널

import sys


INF = sys.maxsize


def solve(N: int, M: int, S: int, T: int, G: list) -> str:
    edges = []
    for u in range(N):
        if not G[u]:
            continue
        min_c, d, v = min(G[u])
        for i in range(len(G[u])):
            c, d, v = G[u][i]
            if min_c == c:
                edges.append((u, v, c, d))

    # Bellman-ford

    dist = [INF] * N
    prev = [[] for _ in range(N)]
    cost = [INF] * N

    dist[S] = 0
    cost[S] = 0

    for _ in range(N):
        for u, v, c, d in edges:
            if cost[v] < cost[u] + c:
                continue
            if cost[v] > cost[u] + c:
                cost[v] = cost[u] + c
                dist[v] = dist[u] + d
                prev[v].clear()
            if dist[v] > dist[u] + d:
                dist[v] = dist[u] + d
            prev[v].append(u)

    if dist[T] == INF:
        return 'VOID'

    visited = [False] * N
    stack = []
    visited[T] = True
    stack.append(T)
    while stack:
        u = stack.pop()
        for v in prev[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

    for _ in range(N):
        for u, v, c, d in edges:
            if (cost[v] > cost[u] + c) and visited[v]:
                cost[v] = cost[u] + c
                dist[v] = dist[u] + d
                return 'UNBOUND'
            if (dist[v] > dist[u] + d) and visited[v]:
                dist[v] = dist[u] + d
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
