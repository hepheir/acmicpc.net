# 7891번: Can you add this?

import sys


N = int(sys.stdin.readline())
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    sys.stdout.write(f'{x+y}\n')
