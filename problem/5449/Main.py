# 5449번: Farmer John

from typing import *
from collections import defaultdict
import heapq
import sys


INF = sys.maxsize
T_Point = Tuple[int, int]
T_Edge = Tuple[T_Point, T_Point]


def solve(bessie: T_Point,
          food: T_Point,
          fences: List[T_Edge]) -> float:
    vertices = set()
    vertices.add(bessie)
    vertices.add(food)
    for p1, p2 in fences:
        vertices.add(p1)
        vertices.add(p2)
    vertices = list(vertices)  # in worst case, total 2N+2 vertices.
    n_vertices = len(vertices)

    graph = defaultdict(list)
    for ui in range(n_vertices):
        u = vertices[ui]
        for vi in range(ui):
            v = vertices[vi]
            for p1, p2 in fences:
                if is_blocking((u, v), (p1, p2)):
                    break
            else:
                graph[u].append((v, length(u, v)))
                graph[v].append((u, length(u, v)))
    for p1, p2 in fences:
        graph[p1].append((p2, length(p1, p2)))
        graph[p2].append((p1, length(p1, p2)))

    dist = defaultdict(lambda: INF)
    heap = []

    dist[bessie] = 0
    heapq.heappush(heap, (dist[bessie], bessie))
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
                heapq.heappush(heap, (dist[v], v))
    return dist[food]


def is_blocking(e1: T_Edge, e2: T_Edge) -> bool:
    # 점과 직선의 내적을 이용해 교차 여부 판단.
    A, B = e1
    C, D = e2
    return (ccw(A, B, C)*ccw(A, B, D) < 0) and (ccw(C, D, A)*ccw(C, D, B) < 0)


def ccw(p1: T_Point, p2: T_Point, p3: T_Point) -> int:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    s = (x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)
    if s > 0:
        s = 1
    if s < 0:
        s = -1
    return s


def length(p1: T_Point, p2: T_Point) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        Bx, By, Fx, Fy = map(int, sys.stdin.readline().split())
        N = int(sys.stdin.readline())
        E = []
        for _ in range(N):
            x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
            E.append(((x1, y1), (x2, y2)))
        answer = solve((Bx, By), (Fx, Fy), E)
        sys.stdout.write(f'{answer:.6f}\n')
