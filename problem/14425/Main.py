# 14425번: 문자열 집합

import sys

N, M = map(int, sys.stdin.readline().split())
S = set()
for _ in range(N):
    S.add(sys.stdin.readline())

ans = 0
for _ in range(M):
    ans += 1 if sys.stdin.readline() in S else 0

print(ans)
