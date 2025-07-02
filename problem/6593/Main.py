# 6593번: 상범 빌딩

import collections
import sys


is_blocked = collections.defaultdict(bool)

queue = collections.deque()
visited = collections.defaultdict(bool)

L: int
R: int
C: int

def is_bound(x, y, z) -> bool:
    return (
        0 <= x < C
        and
        0 <= y < R
        and
        0 <= z < L
    )

def visit(x, y, z):
    if is_bound(x, y, z) and not visited[x, y, z] and not is_blocked[x, y, z]:
        visited[x, y, z] = True
        queue.append((x, y, z))


while True:
    L, R, C = map(int, sys.stdin.readline().split())
    if (L, R, C) == (0, 0, 0):
        break
    queue.clear()
    visited.clear()
    is_blocked.clear()
    sx, sy, sz = None, None, None
    ex, ey, ez = None, None, None
    for z in range(L):
        for y in range(R):
            for x, value in enumerate(sys.stdin.readline().strip()):
                if value == 'S':
                    sx, sy, sz = x, y, z
                if value == 'E':
                    ex, ey, ez = x, y, z
                is_blocked[x, y, z] = (value == '#')
        sys.stdin.readline()
    dist = 0
    answer = None
    visit(sx, sy, sz)
    while queue:
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            if (x, y, z) == (ex, ey, ez):
                answer = dist
                queue.clear()
                break
            visit(x+1, y, z)
            visit(x-1, y, z)
            visit(x, y+1, z)
            visit(x, y-1, z)
            visit(x, y, z+1)
            visit(x, y, z-1)
        dist += 1

    if answer is not None:
        sys.stdout.write(f'Escaped in {answer} minute(s).\n')
    else:
        sys.stdout.write('Trapped!\n')
