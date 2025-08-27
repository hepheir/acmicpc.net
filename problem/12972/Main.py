# 12972번: GCD 테이블

from collections import Counter
from math import gcd
from typing import List
import sys


def solve(counter: Counter, selected: List[int], to_select: int) -> List[int] | None:
    if to_select == 0 and sum(counter.values()) == 0:
        return selected.copy()
    for x in sorted(counter, reverse=True):
        if counter[x] == 0:
            continue
        for y in selected:
            g = gcd(x, y)
            if counter[g] < 2:
                break
        else:
            for y in selected:
                g = gcd(x, y)
                counter[g] -= 2
            counter[x] -= 1
            selected.append(x)
            answer = solve(counter, selected, to_select-1)
            if answer is not None:
                return answer
            selected.pop()
            counter[x] += 1
            for y in selected:
                g = gcd(x, y)
                counter[g] += 2
    return None


N = int(sys.stdin.readline())
G = Counter(map(int, sys.stdin.readline().split()))
print(*solve(G, [], N))
