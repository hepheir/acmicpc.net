# 14619번: 섬 여행

import collections
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

dp = [[-1] * (MAX_K+1) for _ in range(N+1)] # dp[node][hop] = count
queue = collections.deque()
visited = set()
for X in range(1, N+1):
    queue.clear()
    visited.clear()
    queue.append(X)
    visited.add(X)
    for k in range(MAX_K):
        for _ in range(len(queue)):
            u = queue.popleft()
            for v in G[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
        dp[X][k] = len(visited)
        if not queue:
            break
        visited.clear()


T = int(sys.stdin.readline())
for _ in range(T):
    A, K = map(int, sys.stdin.readline().split())
    sys.stdout.write(f'{dp[A][K]}\n')
