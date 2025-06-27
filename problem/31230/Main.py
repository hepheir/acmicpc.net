# 31230번: 모비스터디

import sys
import heapq


MAX_N = 200000
MAX_M = 300000

N, M, A, B = map(int, sys.stdin.readline().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    G[a].append((b, c))
    G[b].append((a, c))


# Dijkstra 최단경로 구하기 O((N+M) log M)

heap = []
dist = [sys.maxsize] * (N+1)
prev = [set() for _ in range(N+1)]

v = A
dist[v] = 0
heapq.heappush(heap, (dist[v], v))
while heap:
    d, u = heapq.heappop(heap)
    if d > dist[u]:
        continue
    for v, w in G[u]:
        if dist[v] > dist[u]+w:
            dist[v] = dist[u]+w
            heapq.heappush(heap, (dist[v], v))
            prev[v].clear()
            prev[v].add(u)
        if dist[v] == dist[u]+w:
            prev[v].add(u)

# 최단 경로상에 존재하는 노드 취합 (그래프 탐색, O(N+M))
visited = [False] * (N+1)
answer = []

sys.setrecursionlimit(10*(MAX_N+MAX_M))
def dfs(u: int):
    visited[u] = True
    answer.append(u)
    for v in prev[u]:
        if not visited[v]:
            dfs(v)

dfs(B)
answer.sort()


# 정답 출력 O(N log N)
print(len(answer))
print(*answer)
