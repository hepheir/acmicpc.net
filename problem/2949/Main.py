# 2949번: 45도

import sys


def rotate(y: int, x: int, deg: int) -> tuple:
    if deg >= 360:
        return rotate(y, x, deg % 360)
    if deg == 0:
        return y, x
    if deg == 45:
        ny = x + y
        nx = x - y
        return ny, nx
    return rotate(x, -y, deg-90)


R, C = map(int, sys.stdin.readline().split())
matrix = [sys.stdin.readline().rstrip() for _ in range(R)]
degree = int(sys.stdin.readline())


min_x = sys.maxsize
min_y = sys.maxsize
max_x = 0
max_y = 0
for y in range(R):
    for x in range(C):
        ny, nx = rotate(y, x, degree)
        max_x = max(nx, max_x)
        max_y = max(ny, max_y)
        min_x = min(nx, min_x)
        min_y = min(ny, min_y)

NR = max_y - min_y + 1
NC = max_x - min_x + 1

answer = [[' '] * NC for _ in range(NR)]
for y in range(R):
    for x in range(C):
        ny, nx = rotate(y, x, degree)
        answer[ny-min_y][nx-min_x] = matrix[y][x]

for y in range(NR):
    row = ''
    for x in range(NC):
        row += answer[y][x]
    print(row.rstrip())
