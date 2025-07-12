# 1417번: 국회의원 선거

import sys
import heapq

N = int(sys.stdin.readline())
my_votes, *other_votes = (int(sys.stdin.readline()) for _ in range(N))
answer = 0

if other_votes:
    max_heap = [-x for x in other_votes]
    heapq.heapify(max_heap)

    while (votes := -heapq.heappop(max_heap)) >= my_votes:
        my_votes += 1
        answer += 1
        heapq.heappush(max_heap, -(votes-1))


print(answer)
