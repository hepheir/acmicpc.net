# 2786번: 상근이의 레스토랑

import sys

MAX_N = int(5e5)
MAX_A = MAX_B = int(1e9)

INF = MAX_A * MAX_N


N = int(sys.stdin.readline())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, sys.stdin.readline().split())


# dp[n]: n개의 음식을 시키기 위한 최소 가격.
dp = [INF] * (N+1)

pq_A = sorted(range(N), key=lambda i: A[i], reverse=True)
pq_B = sorted(range(N), key=lambda i: B[i], reverse=True)

dp[1] = A[pq_A[-1]]

# A를 먼저 뽑는 경우:
acc = 0
for n in range(2, N+1):
    if pq_B[-1] == pq_A[-1]:
        pq_B.pop()
    acc += B[pq_B.pop()]
    dp[n] = min(dp[n], A[pq_A[-1]] + acc)

pq_B = sorted(range(N), key=lambda i: B[i], reverse=True)

# B를 먼저 뽑는 경우:
used = [False] * N
acc = 0
for n in range(2, N+1):
    acc += B[pq_B[-1]]
    used[pq_B[-1]] = True
    pq_B.pop()
    while used[pq_A[-1]]:
        pq_A.pop()
    dp[n] = min(dp[n], A[pq_A[-1]] + acc)

sys.stdout.write('\n'.join(map(str, dp[1:N+1])))
