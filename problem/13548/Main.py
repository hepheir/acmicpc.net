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


counts_per_number = [0] * (MAX_A+1)
numbers_per_count = [0] * (MAX_A+1)
max_count = 0


def cnt_clear():
    global max_count
    for x in range(MAX_A+1):
        counts_per_number[x] = 0
        numbers_per_count[x] = 0
    max_count = 0


def cnt_increase(x: int):
    global max_count
    numbers_per_count[counts_per_number[x]] -= 1
    counts_per_number[x] += 1
    numbers_per_count[counts_per_number[x]] += 1
    if counts_per_number[x] > max_count:
        max_count = counts_per_number[x]


def cnt_decrease(x: int):
    global max_count
    numbers_per_count[counts_per_number[x]] -= 1
    counts_per_number[x] -= 1
    numbers_per_count[counts_per_number[x]] += 1
    while numbers_per_count[max_count] == 0 and max_count > 0:
        max_count -= 1


def cnt_top() -> int:
    return max_count


def mo(queries: List[Query]):
    queries.sort(key=lambda q: q.r)
    l, r = None, None
    cnt_clear()
    for q in queries:
        if l is None and r is None:
            l = q.l
            r = q.r
            for i in range(l, r+1):
                cnt_increase(A[i])
        else:
            while l < q.l:
                cnt_decrease(A[l])
                l += 1
            while l > q.l:
                l -= 1
                cnt_increase(A[l])
            while r < q.r:
                r += 1
                cnt_increase(A[r])
            while r > q.r:
                cnt_decrease(A[r])
                r -= 1
        q.answer = cnt_top()


results: List[Query] = []
for block in QUERIES:
    mo(QUERIES[block])
    results.extend(QUERIES[block])

for q in sorted(results, key=lambda q: q.index):
    sys.stdout.write(f'{q.answer}\n')
