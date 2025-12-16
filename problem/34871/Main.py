# 34871번: Segments

import sys


MAX_N = int(2e6)

min_r = sys.maxsize
max_l = 0

n, q = map(int, sys.stdin.readline().split())
for i in range(n):
    l, r, y = map(int, sys.stdin.readline().split())
    max_l = max(max_l, l)
    min_r = min(min_r, r)

for j in range(q):
    p = int(sys.stdin.readline())
    answer = max(p - min_r, max_l - p, 0)
    print(answer)
