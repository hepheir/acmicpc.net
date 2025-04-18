import collections
import sys

NOT_VISITED = -1


h, w = map(int, sys.stdin.readline().split())
dist = [[NOT_VISITED] * w for _ in range(h)]
sy, sx = 0, 0 # starting point

for y, line in enumerate(sys.stdin.readlines()):
    for x, cell in enumerate(line.split()):
        if cell == '2':
            sy, sx = y, x
        elif cell == '0':
            dist[y][x] = 0

# Breadth first search
q = collections.deque([(sy, sx)])
width = len(q)
depth = 0
while q:
    y, x = q.popleft()
    if y >= 0 and y < h and x >= 0 and x < w and dist[y][x] == NOT_VISITED:
        dist[y][x] = depth
        q.append((y-1, x))
        q.append((y+1, x))
        q.append((y, x-1))
        q.append((y, x+1))
    width -= 1
    if width == 0:
        width = len(q)
        depth += 1

# Print answer
for y in range(h):
    for x in range(w):
        if dist[y][x] == NOT_VISITED:
            print('-1', end=' ')
        else:
            print(dist[y][x], end=' ')
    print()