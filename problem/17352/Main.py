# 17352번: 여러분의 다리가 되어 드리겠습니다!

import sys


N = int(sys.stdin.readline())

G = [[] for _ in range(N+1)]
visited = [False] * (N+1)
stack = []

for _ in range(N-2):
    u, v = map(int, sys.stdin.readline().split())
    G[u].append(v)
    G[v].append(u)


answer = []
for u in range(1, N+1):
    if visited[u]:
        continue
    answer.append(u)
    visited[u] = True
    stack.append(u)
    while stack:
        u = stack.pop()
        for v in G[u]:
            if visited[v]:
                continue
            visited[v] = True
            stack.append(v)

print(*answer)
