from collections import deque
from heapq import heappush

queue = deque(range(10))
heap = []
edited = True
while edited:
    edited = False
    for _ in range(len(queue)):
        x = queue.popleft()
        heappush(heap, x)
        last_digit = x % 10
        for next_digit in range(last_digit):
            queue.append(10 * x + next_digit)
            edited = True


if (N := int(input())) >= len(heap):
    print(-1)
else:
    print(heap[N])
