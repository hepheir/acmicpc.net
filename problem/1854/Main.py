# 1854번: K번째 최단경로 찾기

import heapq
import sys

MAX_N = 1000
MAX_M = 250000
MAX_K = 100

INF = sys.maxsize


N, M, K = map(int, sys.stdin.readline().split())

G = [[] for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    G[a].append((b, c))


# Dijkstra
# dist의 원소는 max heap 이다.
heap = []
dist = [[-INF] * K for _ in range(N+1)]

root = 1
heapq.heappop(dist[root])
heapq.heappush(dist[root], 0)
heapq.heappush(heap, (0, root))

while heap:
    d, u = heapq.heappop(heap)
    if d > -dist[u][0]:
        continue
    for v, w in G[u]:
        if -dist[v][0] > d + w:
            # update dist of node v
            heapq.heappop(dist[v])
            heapq.heappush(dist[v], -(d + w))
            # update heap for graph traverse
            heapq.heappush(heap, (d + w, v))

for u in range(1, N+1):
    if (ans := -dist[u][0]) == INF:
        ans = -1
    sys.stdout.write(f'{ans}\n')
