# 29703번: 펭귄의 하루

from collections import deque
import sys

CELL_START = 'S'
CELL_END = 'H'
CELL_ROUTE = 'F'
CELL_WALL = 'D'

N, M = map(int, sys.stdin.readline().split())
W, H = M, N

grid = [['?'] * W for _ in range(H)]
dist_from_s = [[sys.maxsize] * W for _ in range(H)]
dist_from_e = [[sys.maxsize] * W for _ in range(H)]
routes: list[tuple[int, int]] = []

sx, sy = 0, 0
ex, ey = 0, 0

for y in range(H):
    line = sys.stdin.readline().strip()
    for x in range(W):
        grid[y][x] = line[x]
        if line[x] == CELL_START:
            sx, sy = x, y
        if line[x] == CELL_END:
            ex, ey = x, y
        if line[x] == CELL_ROUTE:
            routes.append((x, y))


def init_shortest_path(x: int, y: int, dist: list[list[int]], directions=[(0, 1), (0, -1), (1, 0), (-1, 0)]):
    q = deque()
    dist[y][x] = 0
    q.append((y, x))
    while q:
        cy, cx = q.popleft()
        for dy, dx in directions:
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < H and 0 <= nx < W):
                continue
            if grid[ny][nx] == CELL_WALL:
                continue
            if dist[ny][nx] > dist[cy][cx] + 1:
                dist[ny][nx] = dist[cy][cx] + 1
                q.append((ny, nx))


init_shortest_path(sx, sy, dist_from_s)
init_shortest_path(ex, ey, dist_from_e)

answer = sys.maxsize
for rx, ry in routes:
    answer = min(answer, dist_from_s[ry][rx] + dist_from_e[ry][rx])

if answer >= sys.maxsize:
    print(-1)
else:
    print(answer)
