from functools import cache
from sys import setrecursionlimit


MAX_T_LEN = 1000
setrecursionlimit(10*MAX_T_LEN)


@cache
def solve(s: str, t: str) -> bool:
    if len(s) == len(t):
        return s == t
    if t[-1] == 'A':
        return solve(s, t[:-1:1])
    if t[-1] == 'B':
        return solve(s, t[-2::-1])
    return False


S = input().strip()
T = input().strip()

if solve(S, T):
    print(1)
else:
    print(0)
