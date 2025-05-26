import sys


MAX_S_LEN = 300000

sys.setrecursionlimit(10*MAX_S_LEN)


def solve(S: str, A: int, B: int, C: int, i: int = 0) -> int:
    if i == len(S):
        return 0
    if S[i] == 'A' and A > 0 and B > 0:
        return solve(S, A-1, B-1, C, i+1)+1
    if S[i] == 'B' and B > 0 and C > 0:
        return solve(S, A, B-1, C-1, i+1)+1
    return solve(S, A, B, C, i+1)


S = sys.stdin.readline().strip()

A = sum([1 for c in S if c == 'A'])
B = sum([1 for c in S if c == 'B'])
C = sum([1 for c in S if c == 'C'])

print(solve(S, A, B, C))
