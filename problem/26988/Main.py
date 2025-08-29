# 26988번: Dollar Dayz

from functools import cache
import sys


@cache
def solve(N: int, K: int) -> int:
    if N == 1 or K == 1:
        return 1
    retval = 0
    for k in range(0, N+1, K):
        retval += solve(N-k, K-1)
    return retval


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    answer = solve(N, K)
    sys.stdout.write(f'{answer}\n')
