# 2786번: 상근이의 레스토랑

import sys
import heapq

MAX_N = int(5e5)
MAX_A = MAX_B = int(1e9)

INF = MAX_A * MAX_N


N = int(sys.stdin.readline())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, sys.stdin.readline().split())

used = [False] * N
heap_A = []
heap_B = []
heap_A_instead_of_B = []
for i in range(N):
    heapq.heappush(heap_A, (A[i], i))
    heapq.heappush(heap_B, (B[i], i))


# dp[n]: n개의 음식을 시키기 위한 최소 가격.
dp = [INF] * (N+1)
dp[1] = heap_A[0][0]

acc_B = 0
for n in range(2, N+1):
    i = heapq.heappop(heap_B)[1]
    acc_B += B[i]
    used[i] = True
    while heap_A and used[heap_A[0][1]]:
        heapq.heappop(heap_A)
    heapq.heappush(heap_A_instead_of_B, (A[i]-B[i], i))

    if heap_A[0][0] < heap_B[0][0] + heap_A_instead_of_B[0][0]:
        dp[n] = acc_B + heap_A[0][0]
    else:
        dp[n] = acc_B + heap_B[0][0] + heap_A_instead_of_B[0][0]

sys.stdout.write('\n'.join(map(str, dp[1:N+1])))
