# 10813번: 공 바꾸기

import sys


N, M = map(int, sys.stdin.readline().split())
baskets = list(range(N+1))

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    baskets[i], baskets[j] = baskets[j], baskets[i]

print(*baskets[1:])
