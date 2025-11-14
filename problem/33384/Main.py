# 33384번: Except One

import sys


def solve(p: int, k: int, t: int) -> int:
    return fast_symmetric_sum_optimal(p, k, t)


def fast_symmetric_sum_optimal(p: int, k: int, t: int) -> int:
    if t >= p - 1:
        return 0
    sign = -1 if t % 2 == 1 else 1
    return (sign * pow(k, t, p)) % p


if __name__ == "__main__":
    p, k, t = map(int, sys.stdin.readline().split())
    answer = solve(p, k, t)
    print(answer)
