# 2976번: NIKOLA

import sys
import heapq


MAX_COST = 500
MAX_N = 1000
INF = MAX_N*MAX_COST


N = int(sys.stdin.readline())
COST = [0] * (N+1)
for i in range(1, N+1):
    COST[i] = int(sys.stdin.readline())


dist = [[INF] * MAX_N for _ in range(N+1)]
heap = [] # (step, dist, node)

step = 0
node = 1
dist[node][step] = 0
heapq.heappush(heap, (step, dist[node][step], node))

while heap:
    u_step, d, u = heapq.heappop(heap)

    if dist[u][u_step] < d:
        continue

    for v, v_step in [(u-u_step, u_step), (u+u_step+1, u_step+1)]:
        if not (1 <= v <= N):
            continue
        if dist[v][v_step] < dist[u][u_step] + COST[v]:
            continue
        dist[v][v_step] = dist[u][u_step] + COST[v]
        heapq.heappush(heap, (v_step, dist[v][v_step], v))

answer = min(dist[N])
print(answer)
