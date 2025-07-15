# 14172번: Moocast

import sys
import math


N = int(sys.stdin.readline())
COWS = []
G = [[] for _ in range(N)]
for i in range(N):
    x, y, p = map(int, sys.stdin.readline().split())
    COWS.append((x, y, p))
    for j in range(i):
        d = math.hypot(COWS[i][0]-COWS[j][0], COWS[i][1]-COWS[j][1])
        if COWS[i][2] >= d:
            G[i].append(j)
        if COWS[j][2] >= d:
            G[j].append(i)


def dfs(u: int, p: int, visited: set):
    visited.add(u)
    answer = 1
    for v in G[u]:
        if v in visited or v == p:
            continue
        answer += dfs(v, u, visited)
    return answer


answer = 0
visited = set()
for i in range(N):
    visited.clear()
    answer = max(answer, dfs(i, None, visited))

print(answer)
