# 15729번: 방탈출

import sys

N = int(sys.stdin.readline())
as_is = [0] * N
to_be = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(N):
    if as_is[i] == to_be[i]:
        continue
    count += 1
    for j in range(i, min(i+3, N)):
        as_is[j] = 1 - as_is[j]

print(count)
