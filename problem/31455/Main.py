from typing import *
import sys


MAX_N = 1024

A: List[List[int]] = [[0] * (MAX_N+1) for _ in range(MAX_N+1)]
A_PS: List[List[int]] = [[0] * (MAX_N+1) for _ in range(MAX_N+1)]  # prefix sum
DR = (0, 0, 1, 1,)
DC = (0, 1, 0, 1,)


def range_sum(r: int, c: int, N: int) -> int:
    return A_PS[r+N-1][c+N-1] - A_PS[r-1][c+N-1] - A_PS[r+N-1][c-1] + A_PS[r-1][c-1]


def solve(r: int, c: int, N: int) -> int:
    "좌상단이 (r, c)인 높이,너비가 N인 쿠기를 먹고 남은 것에 적힌 숫자 총합"
    if N == 1:
        return A[r][c]
    x = range_sum(r, c, N) % 4
    n = N // 2
    sum_numbers = 0
    for i in range(4):
        if i == x:
            continue
        sum_numbers += solve(r+DR[i]*n, c+DC[i]*n, n)
    return sum_numbers


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    for r in range(N):
        for c, number in enumerate(map(int, sys.stdin.readline().strip())):
            A[r][c] = number
            A_PS[r][c] = number + A_PS[r][c-1] + A_PS[r-1][c] - A_PS[r-1][c-1]

    sys.stdout.write(f'{solve(0, 0, N)}\n')
