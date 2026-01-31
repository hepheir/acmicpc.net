# 1189번: 컴백홈

import sys

MAX_R = 5
MAX_C = 5
DX = (-1, 0, 0, 1)
DY = (0, -1, 1, 0)

is_wall = [[False] * MAX_C for _ in range(MAX_R)]
visited = [[False] * MAX_C for _ in range(MAX_R)]

R, C, K = map(int, sys.stdin.readline().split())
for y in range(R):
    for x, value in enumerate(sys.stdin.readline().strip()):
        if value == 'T':
            is_wall[y][x] = True

sx = 0
sy = R - 1

ex = C - 1
ey = 0


def solveBT(y: int, x: int, dist: int) -> int:
    if not (0 <= x < C and 0 <= y < R):
        return 0
    if dist > K:
        return 0
    if visited[y][x]:
        return 0
    if is_wall[y][x]:
        return 0
    if y == ey and x == ex:
        return 1 if (dist == K) else 0
    retval = 0
    visited[y][x] = True
    for dy, dx in zip(DY, DX):
        retval += solveBT(y+dy, x+dx, dist+1)
    visited[y][x] = False
    return retval


print(solveBT(sy, sx, 1))
