# 17608번: 막대기

import sys

N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]

ans = 0
h = -1
while A:
    x = A.pop()
    if x > h:
        h = x
        ans += 1

print(ans)
