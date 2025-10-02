# 15490번: 즐거운 게임

import sys
import functools


MAX_N = 3000

sys.setrecursionlimit(10*MAX_N)


N = int(sys.stdin.readline())
A = list(n for n in map(int, sys.stdin.readline().split()) if n % 2 == 1)
N = len(A)


@functools.lru_cache(maxsize=128*(1024**2))
def can_win(s: int = 0, e: int = N, p1_is_even: bool = 1, p2_is_even: bool = 1) -> bool:
    if s == e:
        return p1_is_even
    if (s+1 < e) and not can_win(s+2, e, p2_is_even, p1_is_even ^ (((A[s]+A[s+1]) % 2) & 1)):
        return True
    if not can_win(s+1, e, p2_is_even, p1_is_even ^ ((A[s] % 2) & 1)):
        return True
    if (s < e-1) and not can_win(s, e-2, p2_is_even, p1_is_even ^ (((A[e-2]+A[e-1]) % 2) & 1)):
        return True
    if not can_win(s, e-1, p2_is_even, p1_is_even ^ ((A[e-1] % 2) & 1)):
        return True
    return False


print('Yes' if can_win() else 'No')
