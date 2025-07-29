# 11290번: Wonowon

import sys
import collections


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

queue = collections.deque()

for p in primes:
    queue.append((1, p))

answer = 0
w_p = 1
while queue:
    for _ in range(len(queue)):
        w, p = queue.popleft()
        if w % p == 0:
            if w_p == p - 2:
                answer += 1
            continue
        if w_p > p - 2:
            continue
        queue.append(((w*100+1)%p, p))
    w_p += 2

print(answer)
