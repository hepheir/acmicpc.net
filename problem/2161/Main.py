from collections import deque

N = int(input())

queue = deque(range(1, N+1))
while queue:
    print(queue.popleft(), end=' ')
    queue.rotate(-1)
