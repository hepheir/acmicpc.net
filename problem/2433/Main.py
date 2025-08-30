# 2433번: The Sound of Silence

import sys
import heapq


max_heap = []
min_heap = []


def sample_append(x: int, expires_at: int) -> int:
    heapq.heappush(min_heap, (+x, expires_at))
    heapq.heappush(max_heap, (-x, expires_at))


def sample_diff(now: int) -> int:
    # assert max_heap
    # assert min_heap
    while max_heap[0][1] <= now:
        heapq.heappop(max_heap)
    while min_heap[0][1] <= now:
        heapq.heappop(min_heap)
    return abs(min_heap[0][0]+max_heap[0][0])


if __name__ == '__main__':
    n, m, c = map(int, sys.stdin.readline().split())
    a = tuple(map(int, sys.stdin.readline().split()))
    silence = []

    for i in range(1, n+1):
        sample_append(a[i-1], i+m)
        if i >= m and sample_diff(i) <= c:
            silence.append(i-m+1)

    if not silence:
        sys.stdout.write('NONE\n')
    else:
        for i in range(len(silence)):
            sys.stdout.write(f'{silence[i]}\n')
