# 6416번: 트리인가?

import collections
import sys


def solve(edges: list) -> bool:
    if not edges:
        return True

    vertices = set()
    graph = collections.defaultdict(list)
    rev_graph = collections.defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        rev_graph[v].append(u)
        vertices.add(u)
        vertices.add(v)

    visited = collections.defaultdict(bool)
    stack = []

    # Finding root via rev-graph traverse
    stack.append(v)
    visited[v] = True
    while stack:
        u = stack.pop()
        if not rev_graph[u]:
            root = u
            break
        for v in rev_graph[u]:
            if visited[v]:
                # only a single path is allowed
                return False
            visited[v] = True
            stack.append(v)

    # Check if all node is reachable via graph traverse
    stack.clear()
    visited.clear()
    stack.append(root)
    visited[root] = True
    while stack:
        u = stack.pop()
        for v in graph[u]:
            if visited[v]:
                # only a single path is allowed
                return False
            visited[v] = True
            stack.append(v)

    for u in vertices:
        if not visited[u]:
            return False

    return True


if __name__ == '__main__':
    tokens = tuple(map(int, sys.stdin.read().split()))
    i = 0
    k = 1
    edges = []
    while i < len(tokens):
        u, v = tokens[i:i+2]
        i += 2
        if (u, v) != (0, 0):
            edges.append((u, v))
            continue
        if (u, v) == (-1, -1):
            break
        if solve(edges):
            sys.stdout.write(f'Case {k} is a tree.\n')
        else:
            sys.stdout.write(f'Case {k} is not a tree.\n')
        k += 1
        edges.clear()
