from functools import cache
from typing import *
import sys


MAX_N = 1024

A: List[List[int]] = [[0] * MAX_N for _ in range(MAX_N)]
DR = (0, 0, 1, 1,)
DC = (0, 1, 0, 1,)


@cache
def get_sum_numbers(r: int, c: int, N: int) -> int:
    # O(N^2)
    if N == 1:
        return A[r][c]
    n = N // 2
    return get_sum_numbers(r+0, c+0, n) \
        + get_sum_numbers(r+0, c+n, n) \
        + get_sum_numbers(r+n, c+0, n) \
        + get_sum_numbers(r+n, c+n, n)


def solve(r: int, c: int, N: int) -> int:
    "좌상단이 (r, c)인 높이,너비가 N인 쿠기를 먹고 남은 것에 적힌 숫자 총합"
    if N == 1:
        return A[r][c]
    x = get_sum_numbers(r, c, N) % 4
    n = N // 2
    sum_numbers = 0
    for i in range(4):
        if i == x:
            continue
        sum_numbers += solve(r+DR[i]*n, c+DC[i]*n, n)
    return sum_numbers


T = int(sys.stdin.readline())
for _ in range(T):
    get_sum_numbers.cache_clear()
    N = int(sys.stdin.readline())
    for r in range(N):
        for c, number in enumerate(map(int, sys.stdin.readline().strip())):
            A[r][c] = number
    answer = solve(0, 0, N)
    sys.stdout.write(f'{answer}\n')
