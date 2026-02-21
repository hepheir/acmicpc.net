# 9711번: 피보나치

import sys

MAX_P = 10000

fib = [0] * (MAX_P+1)
fib[0] = 0
fib[1] = 1
for i in range(2, MAX_P+1):
    fib[i] = fib[i-1] + fib[i-2]

T = int(sys.stdin.readline())
for i in range(1, T+1):
    P, Q = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {fib[P] % Q}')
