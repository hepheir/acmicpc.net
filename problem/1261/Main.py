# 1261번: 알고스팟

import sys
import collections


W, H = map(int, sys.stdin.readline().split())
is_wall = [list(map(int, sys.stdin.readline().strip())) for _ in range(H)]


def adj(y: int, x: int):
    if 0 <= y-1:
        yield y-1, x
    if 0 <= x-1:
        yield y, x-1
    if y+1 < H:
        yield y+1, x
    if x+1 < W:
        yield y, x+1


def solve() -> int:
    queue_empty = collections.deque()
    stack_wall = list()
    visited = [[False] * W for _ in range(H)]
    answer = 0

    queue_empty.append((0, 0))
    visited[0][0] = True

    while True:
        while queue_empty:
            y, x = queue_empty.popleft()
            if (y, x) == (H-1, W-1):
                return answer
            for ny, nx in adj(y, x):
                if visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                if is_wall[ny][nx]:
                    stack_wall.append((ny, nx))
                else:
                    queue_empty.append((ny, nx))
        answer += 1
        while stack_wall:
            y, x = stack_wall.pop()
            is_wall[y][x] = False
            queue_empty.append((y, x))


answer = solve()
print(answer)
