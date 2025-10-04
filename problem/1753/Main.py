# 1753번: 최단경로

import sys
import heapq
import collections


INF = sys.maxsize


graph = collections.defaultdict(list)
dist = collections.defaultdict(lambda: INF)


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))


heap = []
dist[K] = 0
heapq.heappush(heap, (dist[K], K))

while heap:
    d, u = heapq.heappop(heap)
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(heap, (dist[v], v))


for i in range(1, V+1):
    print(dist[i] if dist[i] < INF else 'INF')
