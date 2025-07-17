# 14619번: 섬 여행

from collections import deque
from functools import cache
from typing import List
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


@cache
def get_min_height_per_moves(node: int) -> List[int]:
    # 반환값의 k번째 인덱스는 node 로 부터 k번 다리를 건넜을 때,
    # 방문할 수 있는 노드들 중 가장 작은 높이.
    # O(N^2 K)
    min_height = [-1] * (MAX_K+1)

    queue = deque()
    dist = [-1] * (N+1)

    d = 0
    queue.append(node)
    dist[node] = d
    min_height[d] = H[node]

    while queue and (d := d+1) <= MAX_K:
        for _ in range(len(queue)):
            u = queue.popleft()
            for v in G[u]:
                if dist[v] >= d:
                    continue
                dist[v] = d
                queue.append(v)
                if (min_height[d] == -1) or (min_height[d] > H[v]):
                    min_height[d] = H[v]

    return min_height


T = int(sys.stdin.readline())
for _ in range(T):
    A, K = map(int, sys.stdin.readline().split())
    answer = get_min_height_per_moves(A)[K]
    sys.stdout.write(f'{answer}\n')
