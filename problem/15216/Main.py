# 15216번: Another Brick in the Wall

import sys


H, W, N = map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))

def solve() -> bool:
    w = W
    h = H
    for i in range(N):
        w -= X[i]
        if w == 0:
            w = W
            h -= 1
            if h == 0:
                return True
        if w < 0:
            return False
    return False


if solve():
    print('YES')
else:
    print('NO')