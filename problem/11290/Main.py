# 11290번: Wonowon

import sys


N = int(sys.stdin.readline())

primes = []
sieve = [True] * (N+1)
sieve[0] = False
sieve[1] = False
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(i*i, N+1, i):
            sieve[j] = False

for i in range(2, N+1):
    if sieve[i]:
        primes.append(i)


def W(p: int) -> int:
    if p == 2 or p == 5:
        return -1
    retval = 1
    w = 1
    while w % p:
        w = (w*100+1) % p
        retval += 2
    return retval


answer = 0
for p in primes:
    if W(p) == p-2:
        answer += 1

print(answer)
