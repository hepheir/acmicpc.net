from typing import *
from collections import deque
import sys


MAX_CAPACITY = 100000

queue = deque()
visited = [False] * (MAX_CAPACITY+1)

for _ in range(3):
    N = int(sys.stdin.readline())

    for n in range(N//2+1):
        visited[n] = False
    queue.clear()


    capacity = 0
    queue.append(0)

    for i in range(N):
        unit, count = map(int, sys.stdin.readline().split())
        capacity += unit * count
        for _ in range(count):
            for _ in range(len(queue)):
                x = queue.popleft()
                y = x+unit
                if not visited[y]:
                    visited[y] = True
                    queue.append(y)
                queue.append(x)
    if capacity % 2 == 0 and visited[capacity//2]:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
