# 1405번: 미친 로봇

import sys

sys.setrecursionlimit(int(1e5))

N, Ep, Wp, Sp, Np = map(int, input().split())

Ep = Ep * 0.01
Wp = Wp * 0.01
Sp = Sp * 0.01
Np = Np * 0.01


def backtrack(x: int, y: int, prob: float, life: int, visited: set) -> float:
    if life == 0:
        return 1
    retval = 0
    visited.add((x, y))
    if (x+1, y) not in visited:
        retval += Ep * backtrack(x+1, y, prob, life-1, visited)
    if (x-1, y) not in visited:
        retval += Wp * backtrack(x-1, y, prob, life-1, visited)
    if (x, y+1) not in visited:
        retval += Np * backtrack(x, y+1, prob, life-1, visited)
    if (x, y-1) not in visited:
        retval += Sp * backtrack(x, y-1, prob, life-1, visited)
    visited.discard((x, y))
    return retval


answer = backtrack(0, 0, 1.0, N, set())
print(answer)
