import heapq
import sys


N, K = map(int, sys.stdin.readline().split())
WORDS = []


def calc_edge_cost(u: int, v: int) -> int:
    cost = 0
    for cu, cv in zip(WORDS[u], WORDS[v]):
        cost += abs(ord(cu) - ord(cv))
    return cost


rank = list(range(N))


def union(u: int, v: int):
    u = find(u)
    v = find(v)
    if u > v:
        u, v = v, u
    rank[v] = rank[u]


def find(u: int) -> int:
    if rank[u] != rank[rank[u]]:
        rank[u] = find(rank[u])
    return rank[u]


heap = []
for u in range(N):
    word = sys.stdin.readline().strip()
    WORDS.append(word)
    for v in range(u):
        w = calc_edge_cost(u, v)
        heapq.heappush(heap, (w, u, v))

max_w = 0
while heap:
    w, u, v = heapq.heappop(heap)
    if find(u) != find(v):
        union(u, v)
        if w > max_w:
            max_w = w

print(max_w)
