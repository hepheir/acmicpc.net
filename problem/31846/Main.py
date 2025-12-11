# 31846번: 문자열 접기

import functools
import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()


@functools.lru_cache(maxsize=None)
def get_score(s: int, e: int) -> int:
    """
    s: inclusive
    e: exclusive
    """
    assert s < e
    assert (e-s) % 2 == 0
    score = 0
    while s < e:
        if S[s] == S[e-1]:
            score += 1
        s += 1
        e -= 1
    return score


P = int(sys.stdin.readline())
for _ in range(P):
    l, r = map(int, sys.stdin.readline().split())
    answer = 0
    for pivot in range(l+1, r):
        size = min(pivot-l, r-pivot+1)
        s = pivot-1-size
        e = pivot-1+size
        answer = max(answer, get_score(s, e))
    print(answer)
