# 30828번: 셰프 건공이

import functools
import sys


INF = sys.maxsize
MAX_N = 500
MAX_T = 511

sys.setrecursionlimit(100*MAX_N)


N = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))


@functools.cache
def solve(l: int, r: int) -> int:
    return max(max_xor(l, r, k)+k for k in range(r-l+2))


@functools.cache
def max_xor(l: int, r: int, k: int) -> int:
    """[l,r] 구간의 숫자 중 k개를 xor하여 얻을 수 있는 최대 숫자.
    20,958,500가지 경우의 수 존재.
    """
    if k == 0:
        return 0
    if l > r:
        return -INF
    return max(max_xor(l, r-1, k), max_xor(l, r-1, k-1)^T[r-1])


Q = int(sys.stdin.readline())
for _ in range(Q):
    l, r = map(int, sys.stdin.readline().split())
    sys.stdout.write(f'{solve(l, r)}\n')
