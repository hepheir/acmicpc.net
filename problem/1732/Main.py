# 1732번: 레이저

from collections import defaultdict
from typing import List, Tuple
from math import hypot, gcd
import sys


def solve(N: int, LASERS: List[Tuple[int, int, int]]) -> List[Tuple[int, int]]:
    lasers_per_vector = defaultdict(list)
    for x, y, h in LASERS:
        # (x, y) 벡터의 크기
        l = hypot(x, y)
        # (x, y) 벡터의 방향벡터
        ux, uy = x//gcd(x, y), y//gcd(x, y)
        lasers_per_vector[ux, uy].append((x, y, h, l))

    invisible_lasers = []
    for ux, uy in lasers_per_vector:
        lasers = lasers_per_vector[ux, uy]
        max_height = -1
        for x, y, h, l in sorted(lasers, key=lambda laser: laser[3]):
            if max_height < h:
                max_height = h
            else:
                invisible_lasers.append((x, y))

    return invisible_lasers


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    LASERS = []
    for _ in range(N):
        x, y, z = map(int, sys.stdin.readline().split())
        LASERS.append((x, y, z))
    for x, y in sorted(solve(N, LASERS)):
        sys.stdout.write(f'{x} {y}\n')
