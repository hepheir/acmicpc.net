# 13265번: 색칠하기

import collections
import sys

MAX_N = 1000


def solve(n: int, m: int, edges: list) -> str:
    G = [[] for _ in range(n+1)]
    for i in range(m):
        x, y = edges[i]
        G[x].append(y)
        G[y].append(x)

    visited = [False] * (n+1)
    color = [None] * (n+1)
    queue = collections.deque()

    for u in range(1, n+1):
        if visited[u]:
            continue
        visited[u] = True
        color[u] = True
        queue.append(u)
        while queue:
            u = queue.popleft()
            for v in G[u]:
                if visited[v]:
                    if color[u] == color[v]:
                        return 'impossible'
                    continue
                visited[v] = True
                color[v] = not color[u]
                queue.append(v)
    return 'possible'


T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    E = []
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        E.append((x, y))
    answer = solve(n, m, E)
    sys.stdout.write(f'{answer}\n')
