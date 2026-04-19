# 3976번: 역습

from dataclasses import dataclass
from typing import List
import sys


@dataclass
class Striker:
    lp: int # long pass
    s: int # shoot
    p: List[int] # pass
    d: List[int] # dribble


def solve(N: int, s1: Striker, s2: Striker) -> int:
    # 1. 수비수 -> 스트라이커(1/2): 긴 패스
    # 2. 스트라이커(1/2) -> : 드리블 or 다른 스트라이커에게 패스
    # 3. n점에서 스트라이커가 슛

    # Bottom-up DP
    p1, p2 = s1.lp, s2.lp  # 각 스트라이커 별 누적 난이도.
    for i in range(N-1):
        p1, p2 = min(p1 + s1.d[i], p2 + s2.p[i]), min(p2 + s2.d[i], p1 + s1.p[i])

    return min(p1 + s1.s, p2 + s2.s)


c = int(sys.stdin.readline())
for _ in range(c):
    n, l1, l2, s1, s2 = map(int, sys.stdin.readline().split())
    p1 = list(map(int, sys.stdin.readline().split()))
    d1 = list(map(int, sys.stdin.readline().split()))
    p2 = list(map(int, sys.stdin.readline().split()))
    d2 = list(map(int, sys.stdin.readline().split()))

    striker1 = Striker(l1, s1, p1, d1)
    striker2 = Striker(l2, s2, p2, d2)

    print(solve(n, striker1, striker2))
