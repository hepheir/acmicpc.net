# 33219번: Avant-garde

import sys


def circle_height(cx: int, cr: int, x: float) -> float:
    """임의의 x좌표에서의 원의 높이"""
    if not (cx-cr < x < cx+cr):
        return 0
    return (cr**2 - (x-cx)**2)**0.5


def f(x: float) -> float:
    """특정 x좌표에서의 최대 y값"""
    max_y = 0
    for i in range(n):
        cx, cr = blobs[i]
        y = circle_height(cx, cr, x)
        if max_y < y:
            max_y = y
    return max_y


n = int(sys.stdin.readline())
blobs = []
for i in range(n):
    x, r = map(int, sys.stdin.readline().split())
    blobs.append((x, r))

F = 0
dx = 0.1
x = -20
while x <= 20:
    F += 2*f(x)*dx
    x += dx
print(F)
