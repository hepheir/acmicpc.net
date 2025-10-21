# 30007번: 라면 공식

import sys


N = int(sys.stdin.readline())
for _ in range(N):
    A, B, X = map(int, sys.stdin.readline().split())
    W = A*(X-1)+B
    print(W)
