# 4811번: 알약

import functools
import sys


@functools.cache
def solve(P: int, H: int) -> int:
    # P: 온전한 알약 개수, H: 반쪽 짜리 알약 개수
    if P < 0 or H < 0:
        return 0
    if P + H == 0:
        return 1
    return solve(P-1, H+1) + solve(P, H-1)


while (N := int(sys.stdin.readline())):
    print(solve(N, 0))
