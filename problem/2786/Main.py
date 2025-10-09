# 2786번: 상근이의 레스토랑

import sys


N = int(sys.stdin.readline())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, sys.stdin.readline().split())

pq_A = sorted(range(N), key=lambda i: A[i], reverse=True)
pq_B = sorted(range(N), key=lambda i: B[i], reverse=True)
used = [False] * N

answers = [-1] * (N+1)
answers[1] = A[pq_A[-1]]
for n in range(2, N+1):
    answers[n] = answers[n-1]

    used[pq_B[-1]] = True
    answers[n] -= A[pq_A[-1]]
    answers[n] += B[pq_B[-1]]
    pq_B.pop()

    while used[pq_A[-1]]:
        pq_A.pop()
    answers[n] += A[pq_A[-1]]

sys.stdout.write('\n'.join(map(str, answers[1:N+1])))
