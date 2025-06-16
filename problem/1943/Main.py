from typing import *
from collections import deque
import sys


MAX_CAPACITY = 100000

queue = deque()
visited = [False] * (MAX_CAPACITY+1)

for _ in range(3):
    N = int(sys.stdin.readline())

    queue.clear()
    for n in range(N//2+1):
        visited[n] = False
    queue.append(0)
    visited[0] = True

    coins = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    coins.sort(reverse=True)

    capacity = [unit*count for unit, count in coins]
    capacity_ps = capacity.copy() # prefix sum
    for i in range(1, N):
        capacity_ps[i] += capacity_ps[i-1]

    if capacity_ps[N-1] % 2 == 0:
        for i in range(N):
            unit, count = coins[i]
            for _ in range(count):
                for _ in range(len(queue)):
                    x = queue.popleft()
                    if (capacity_ps[N-1] - capacity_ps[i]) <= x <= (capacity_ps[N-1]):
                        queue.append(x)
                    y = x+unit
                    if (capacity_ps[N-1] - capacity_ps[i]) <= y <= (capacity_ps[N-1]):
                        if not visited[y]:
                            visited[y] = True
                            queue.append(y)

    if visited[capacity_ps[N-1]//2]:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
