from typing import List
import sys
import heapq


def solve(V: int, E: int, heights: List[int], edges: List[int]) -> List[int]:
    # 더 낮은 쉼터로만 이어지는 방향 그래프 구축
    G = [[] for _ in range(V+1)]
    for u, v in edges:
        if heights[u] < heights[v]:
            G[v].append(u)
        if heights[u] > heights[v]:
            G[u].append(v)
    dist = [1] * (V+1)
    # 고도 높은 순
    heap = [] # (height, dist, node)
    for u in range(1, V+1):
        heapq.heappush(heap, (-heights[u], dist[u], u))
    while heap:
        inv_h, d, u = heapq.heappop(heap)
        if dist[u] > d:
            continue
        for v in G[u]:
            if dist[v] < d+1:
                dist[v] = d+1
                heapq.heappush(heap, (-heights[v], dist[v], v))
    return dist


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    A = [None, *map(int, sys.stdin.readline().split())]
    B = [tuple(map(int, sys.stdin.readline().split())) for i in range(M)]
    dist = solve(N, M, A, B)
    for i in range(1, N+1):
        sys.stdout.write(f'{dist[i]}\n')
