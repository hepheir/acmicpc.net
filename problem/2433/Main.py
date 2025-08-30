# 2433번: The Sound of Silence

import sys
import heapq


n, m, c = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

max_heap = []
min_heap = []

silence = []

i = 0
while i < n:
    heapq.heappush(min_heap, (a[i], i))
    heapq.heappush(max_heap, (-a[i], i))

    while max_heap[0][1] <= i-m:
        heapq.heappop(max_heap)
    while min_heap[0][1] <= i-m:
        heapq.heappop(min_heap)

    if i >= m and abs(min_heap[0][0]+max_heap[0][0]) <= c:
        silence.append(i+1-m+1)

    i += 1


if not silence:
    print('NONE')
else:
    print('\n'.join(map(str, silence)))
