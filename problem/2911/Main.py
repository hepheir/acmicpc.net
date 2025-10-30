# 2911번: 전화 복구

import sys


def solve(N: int, M: int, P: list, C: list) -> int:
    answer = 0
    i_ordered = sorted(range(N), key=lambda i: P[i])
    # zero-padding
    P.append(0)
    C.append(0)
    prev_i = -1
    for curr_i in i_ordered:
        dc = C[curr_i] - C[prev_i]
        if dc > 0:
            answer += dc
        prev_i = curr_i
    return answer


N, M = map(int, sys.stdin.readline().split())
P = [0] * N
C = [0] * N
for i in range(N):
    P[i], C[i] = map(int, sys.stdin.readline().split())
print(solve(N, M, P, C))
