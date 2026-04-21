# 5545번: 최고의 피자

import sys


N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
D = [0] * N
for i in range(N):
    D[i] = int(sys.stdin.readline())


value = C  # 피자 열량
cost = A  # 피자 가격
max_ratio = value / cost  # 1원 당 열량

# Greedy Let's go
for i in sorted(range(N), key=lambda i: D[i], reverse=True):
    value += D[i]
    cost += B

    if max_ratio < (ratio := value / cost):
        max_ratio = ratio


print(int(max_ratio))
