from collections import deque
from functools import cache
import sys

IMPOSSIBLE = 'Impossible'
MAX_X = 100

pool = []


@cache
def solve(X: int) -> int:
    min_dist = sys.maxsize
    queue = deque(pool)
    for dist in range(1, 4):
        for _ in range(len(queue)):
            x = queue.popleft()
            if x > X:
                continue
            if x == X:
                return dist
            if x >= 2 and X % x == 0:
                min_dist = min(min_dist, dist + 1 + solve(X // x))
            for y in pool:
                queue.append(10*x+y)
    return min_dist


T = int(sys.stdin.readline())
for case in range(1, T+1):
    solve.cache_clear()
    pool.clear()
    for x, is_available in enumerate(map(int, sys.stdin.readline().split())):
        if is_available:
            pool.append(x)
    X = int(sys.stdin.readline())

    if (dist := solve(X)) >= sys.maxsize:
        dist = IMPOSSIBLE
    else:
        dist += 1
    sys.stdout.write(f'Case #{case}: {dist}\n')
