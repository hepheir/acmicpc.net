from typing import Dict, List
from collections import defaultdict
import sys
import dataclasses


MAX_A = 100000


@dataclasses.dataclass
class Query:
    index: int
    l: int
    r: int
    answer: int = None


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

# Mo's Query Sqrt Decomposition
SQRT_N = int(N ** 0.5)
QUERIES: Dict[int, List[Query]] = defaultdict(list)
for i in range(M):
    l, r = map(int, sys.stdin.readline().split())
    query = Query(index=i, l=l-1, r=r-1)
    QUERIES[l // SQRT_N].append(query)


range_max_tree = [0] * (4*MAX_A)


def rmt_clear():
    for i in range(N):
        rmt_update(A[i], value=0)


def rmt_top() -> int:
    return range_max_tree[1]


def rmt_increase(index: int):
    rmt_update(index, diff=1)


def rmt_decrease(index: int):
    rmt_update(index, diff=-1)


def rmt_update(index: int, diff: int = None, value: int = None):
    def rmt_update_util(node: int, node_lo: int, node_hi: int):
        if index < node_lo or node_hi < index:
            return
        if node_lo == node_hi:
            if diff is not None:
                range_max_tree[node] += diff
            if value is not None:
                range_max_tree[node] = value
            return
        node_mid = (node_lo+node_hi)//2
        rmt_update_util(2*node, node_lo, node_mid)
        rmt_update_util(2*node+1, node_mid+1, node_hi)
        range_max_tree[node] = max(
            range_max_tree[2*node],
            range_max_tree[2*node+1],
        )
    rmt_update_util(1, 1, MAX_A)


def mo(queries: List[Query]):
    queries.sort(key=lambda q: q.r)
    l, r = None, None
    rmt_clear()
    for q in queries:
        if l is None and r is None:
            l = q.l
            r = q.r
            for i in range(l, r+1):
                rmt_increase(A[i])
        else:
            while l < q.l:
                rmt_decrease(A[l])
                l += 1
            while l > q.l:
                l -= 1
                rmt_increase(A[l])
            while r < q.r:
                r += 1
                rmt_increase(A[r])
            while r > q.r:
                rmt_decrease(A[r])
                r -= 1
        q.answer = rmt_top()


results: List[Query] = []
for block in QUERIES:
    mo(QUERIES[block])
    results.extend(QUERIES[block])

for q in sorted(results, key=lambda q: q.index):
    sys.stdout.write(f'{q.answer}\n')
