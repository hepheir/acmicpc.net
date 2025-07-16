# 30625번: 댄스타임

import sys


MOD = int(1e9)+7

N, M = map(int, sys.stdin.readline().split())

dp_curr = [1, 0]
dp_prev = [0, 0]

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())

    if B == 0:
        success, fail = 1, M-1
    else:
        success, fail = M-1, 1

    dp_curr, dp_prev = dp_prev, dp_curr
    dp_curr[0] = (success * dp_prev[0]) % MOD
    dp_curr[1] = (success * dp_prev[1] + fail * dp_prev[0]) % MOD

answer = sum(dp_curr) % MOD

print(answer)
