# 7576번: 토마토

import collections
import sys


INF = sys.maxsize

TOMATO_RIPEN = '1'
TOMATO_RAW = '0'
TOMATO_EMPTY = '-1'

DX = (0, 0, 1, -1)
DY = (1, -1, 0, 0)


M, N = map(int, sys.stdin.readline().split())

queue = collections.deque()  # 갓 익었을 때.
should_be_visited = collections.defaultdict(bool)
raw_tomato_count = 0

for y in range(N):
    row = sys.stdin.readline().split()
    for x in range(M):
        if row[x] == TOMATO_RIPEN:
            should_be_visited[y, x] = False
            queue.append((y, x))
        if row[x] == TOMATO_RAW:
            should_be_visited[y, x] = True
            raw_tomato_count += 1
        if row[x] == TOMATO_EMPTY:
            should_be_visited[y, x] = False


day = -1
while queue:
    day += 1
    for _ in range(len(queue)):
        y, x = queue.popleft()
        for dy, dx in zip(DY, DX):
            ny = y+dy
            nx = x+dx
            if not (0 <= nx < M and 0 <= ny < N):
                continue
            if not should_be_visited[ny, nx]:
                continue
            should_be_visited[ny, nx] = False
            raw_tomato_count -= 1
            queue.append((ny, nx))

if raw_tomato_count > 0:
    print(-1)
else:
    print(day)
