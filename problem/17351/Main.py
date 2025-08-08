# 17351번: 3루수는 몰라

import sys
import functools


N = int(sys.stdin.readline())
GRID = [sys.stdin.readline() for _ in range(N)]


@functools.cache
def count_MOLA(x: int = 0, y: int = 0, expect: str = 'M') -> int:
    # O(4*N^2) ~= 1M의 경우의 수. -> TLE, MLE 걱정 없음.
    count = 0
    if y == N or x == N:
        pass
    elif GRID[y][x] == expect:
        if expect == 'M':
            count = max(count_MOLA(x+1, y, 'O'), count_MOLA(x, y+1, 'O'))
        elif expect == 'O':
            count = max(count_MOLA(x+1, y, 'L'), count_MOLA(x, y+1, 'L'))
        elif expect == 'L':
            count = max(count_MOLA(x+1, y, 'A'), count_MOLA(x, y+1, 'A'))
        elif expect == 'A':
            count = max(count_MOLA(x+1, y), count_MOLA(x, y+1)) + 1
    else:
        count = max(count_MOLA(x+1, y), count_MOLA(x, y+1))
    return count


# pre-cache to avoid max-recursion limit.
for y in reversed(range(N)):
    for x in reversed(range(N)):
        count_MOLA(x, y)


print(count_MOLA())
