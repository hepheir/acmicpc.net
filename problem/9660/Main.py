# 9660번: 돌 게임 6

import sys
from functools import cache

PERIOD = 7


@cache
def can_win(N: int) -> bool:
    # O(3^N) -> O(N)
    if N >= 4 and not can_win(N-4):
        return True
    if N >= 3 and not can_win(N-3):
        return True
    if N >= 1 and not can_win(N-1):
        return True
    return False


def optimized_can_win(N: int) -> bool:
    return can_win(N % PERIOD)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    print('SK' if optimized_can_win(N) else 'CY')
