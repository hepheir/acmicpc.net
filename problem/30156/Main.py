# 30156번: Malvika is peculiar about color of balloons

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    S = sys.stdin.readline().strip()
    a, b = 0, 0
    for c in S:
        if c == 'a':
            a += 1
        else:
            b += 1
    print(min(a, b))
