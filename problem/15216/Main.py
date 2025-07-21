# 15216번: Another Brick in the Wall

import sys


H, W, N = map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))

answer = 'NO'
w = W
h = H
for i in range(N):
    w -= X[i]
    if w == 0:
        w = W
        h -= 1
        if h == 0:
            answer = 'YES'
            break
    if w < 0:
        break

print(answer)
