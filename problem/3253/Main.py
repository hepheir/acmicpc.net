# 3253번: TRAM

import heapq
import sys


INF = sys.maxsize

N, A, B = map(int, sys.stdin.readline().split())
K = [0] * (N+1)
OUT = [0] * (N+1)
INS = [[] for _ in range(N+1)]
for i in range(1, N+1):
    args = list(map(int, sys.stdin.readline().split()))
    K[i] = args[0]
    if K[i] >= 1:
        OUT[i] = args[1]
    if K[i] >= 2:
        INS[i] = args[2:]


# Dijkstra

heap = []
dist = [INF] * (N+1)

dist[A] = 0
heapq.heappush(heap, (dist[A], A))

while heap:
    d, u = heapq.heappop(heap)
    if dist[u] < d:
        continue

    # OUT[u] 방향으로는 스위치 전환 없이 이동할 수 있음.
    v = OUT[u]
    if dist[v] > dist[u]:
        dist[v] = dist[u]
        heapq.heappush(heap, (dist[v], v))

    # 그 외에는 스위치를 조작해야만 갈 수 있다.
    for v in INS[u]:
        if dist[v] > dist[u] + 1:
            dist[v] = dist[u] + 1
            heapq.heappush(heap, (dist[v], v))

if dist[B] == INF:
    print('-1')
else:
    print(dist[B])
