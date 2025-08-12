# 30828번: 셰프 건공이

import sys

INF = sys.maxsize

MAX_N = 500
MAX_T = 511
MAX_Q = 100000


N = int(sys.stdin.readline())
T = [None, *map(int, sys.stdin.readline().split())]


answer = [[0] * (N+1) for _ in range(N+1)]

for l in range(1, N+1):
    # curr[i] = 임의의 원소들을 XOR 하여 i를 만들기 위한 최소 원소 개수
    curr = [INF] * (MAX_T+1)
    prev = [INF] * (MAX_T+1)
    curr[0] = 0
    xor_value = 0
    xor_count = 0
    for r in range(l, N+1):
        xor_value ^= T[r]
        xor_count += 1
        prev, curr = curr, prev
        for i in range(MAX_T+1):
            curr[i] = min(prev[i], prev[i^T[r]]+1)
        answer[l][r] = max((xor_value^i)-curr[i] for i in range(MAX_T+1)) + xor_count


Q = int(sys.stdin.readline())
for _ in range(Q):
    l, r = map(int, sys.stdin.readline().split())
    sys.stdout.write(f'{answer[l][r]}\n')
