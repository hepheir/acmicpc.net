from typing import Dict, List
from collections import defaultdict
import sys
import dataclasses


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


def mo(queries: List[Query]):
    queries.sort(key=lambda q: q.r)
    counter = defaultdict(int)
    count_unique = 0
    l, r = None, None
    for q in queries:
        if l is None and r is None:
            l = q.l
            r = q.r
            for i in range(l, r+1):
                if counter[A[i]] == 0:
                    count_unique += 1
                counter[A[i]] += 1
        else:
            while l < q.l:
                counter[A[l]] -= 1
                if counter[A[l]] == 0:
                    count_unique -= 1
                l += 1
            while l > q.l:
                l -= 1
                if counter[A[l]] == 0:
                    count_unique += 1
                counter[A[l]] += 1
            while r < q.r:
                r += 1
                if counter[A[r]] == 0:
                    count_unique += 1
                counter[A[r]] += 1
            while r > q.r:
                counter[A[r]] -= 1
                if counter[A[r]] == 0:
                    count_unique -= 1
                r -= 1
        q.answer = count_unique


results: List[Query] = []
for block in QUERIES:
    mo(QUERIES[block])
    results.extend(QUERIES[block])
results.sort(key=lambda q: q.index)

for q in results:
    sys.stdout.write(f'{q.answer}\n')
