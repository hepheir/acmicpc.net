# 2129번: 드라이브 파이널

from typing import *
import sys


INF = sys.maxsize


def solve(N: int, M: int, S: int, T: int, E: List[Tuple[int, int, int, int, int]]) -> str:
    graph, vertices, source, sink = init_directed_graph(N, M, S, T, E)
    graph = filter_edges(graph, vertices)
    used_vertices = filter_vertices(graph, vertices, source, sink)
    distance, fatigue, is_negative_cycle = bellman_ford(graph, vertices, source)

    if not used_vertices[sink]:
        return 'VOID'

    for u in vertices:
        if used_vertices[u] and is_negative_cycle[u]:
            return 'UNBOUND'

    return f'{fatigue[sink]} {distance[sink]}'


def init_directed_graph(N: int, M: int, S: int, T: int, E: List[Tuple[int, int, int, int, int]]) -> Tuple[Dict[int, List[Tuple[int, int, int]]], List[int]]:
    """인접 리스트 생성"""
    vertices = list(range(N))
    source = S
    sink = T
    graph = {u: [] for u in vertices}
    for i in range(M):
        u, v, fatigue_uv, distance, fatigue_vu = E[i]
        graph[u].append((v, fatigue_uv, distance))
        graph[v].append((u, fatigue_vu, distance))
    return graph, vertices, source, sink


def filter_edges(graph: Dict[int, List[Tuple[int, int, int]]], vertices: List[int]) -> Dict[int, List[Tuple[int, int, int]]]:
    """이동 가능한 도로만 남기기"""
    retval = {u: [] for u in vertices}
    for u in vertices:
        if not graph[u]:
            continue
        min_fatigue = min(graph[u], key=lambda e: e[1])[1]
        for v, fatigue, distance in graph[u]:
            if fatigue == min_fatigue:
                retval[u].append((v, fatigue, distance))
    return retval


def filter_vertices(graph: Dict[int, List[Tuple[int, int, int]]], vertices: List[int], source: int, sink: int) -> Dict[int, bool]:
    stack = []
    # Graph Traverse
    visited = {u: False for u in vertices}
    stack.append(source)
    visited[source] = True
    while stack:
        u = stack.pop()
        for v, fatigue, distance in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    # Reversed Graph Traverse
    graph_rev = {u: [] for u in vertices}
    for u in vertices:
        for v, fatigue, distance in graph[u]:
            graph_rev[v].append((u, fatigue, distance))
    visited_rev = {u: False for u in vertices}
    stack.append(sink)
    visited_rev[sink] = True
    while stack:
        u = stack.pop()
        for v, fatigue, distance in graph_rev[u]:
            if not visited_rev[v]:
                visited_rev[v] = True
                stack.append(v)
    return {u: (visited[u] and visited_rev[u]) for u in vertices}


def bellman_ford(graph: Dict[int, List[Tuple[int, int, int]]], vertices: List[int], source: int):
    # Bellman-ford, O(VE)
    edges = []
    for u in vertices:
        for v, f, d in graph[u]:
            edges.append((u, v, f, d))

    distance = {u: INF for u in vertices}
    fatigue = {u: INF for u in vertices}
    is_negative_cycle = {u: False for u in vertices}

    distance[source] = 0
    fatigue[source] = 0

    # Repeat relaxation
    for _ in range(len(vertices)):
        for u, v, f, d in edges:
            if (fatigue[v] > fatigue[u] + f):
                fatigue[v] = fatigue[u] + f
                distance[v] = distance[u] + d
                continue
            if (fatigue[v] == fatigue[u] + f) and (distance[v] > distance[u] + d):
                distance[v] = distance[u] + d
                continue

    # Find negative cycle
    for u, v, f, d in edges:
        if (fatigue[v] > fatigue[u] + f):
            fatigue[v] = fatigue[u] + f
            distance[v] = distance[u] + d
            is_negative_cycle[v] = True
            continue
        if (fatigue[v] == fatigue[u] + f) and (distance[v] > distance[u] + d):
            distance[v] = distance[u] + d
            continue

    return distance, fatigue, is_negative_cycle


if __name__ == '__main__':
    N, M, S, T = map(int, sys.stdin.readline().split())
    E = []
    for _ in range(M):
        u, v, a, c, b = map(int, sys.stdin.readline().split())
        E.append((u, v, a, c, b))
    answer = solve(N, M, S, T, E)
    print(answer)
