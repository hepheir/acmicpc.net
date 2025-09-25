# 4703번: 그림의 추측

from collections import defaultdict
from typing import *
import sys


MAX_H = int(1e10)
MAX_PRIMES = int(MAX_H**0.5)

is_prime = [True] * (MAX_PRIMES+1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(MAX_PRIMES**0.5)+1):
    if not is_prime[i]:
        continue
    for j in range(i*i, MAX_PRIMES+1, i):
        is_prime[j] = False

primes = []
for i in range(2, MAX_PRIMES+1):
    if is_prime[i]:
        primes.append(i)


def solve(L: int, H: int) -> str:
    # L..H 구간이 합성수이려면 그 구간의 크기는 생각보다 크지 않을 것.
    choices = defaultdict(list)
    for p, numbers in find_divisible(L, H):
        for number in numbers:
            choices[number].append(p)

    used = defaultdict(bool)
    stack = []

    def backtrack(n: int) -> bool:
        if len(stack) == (H-L+1):
            return True
        for prime in choices[n]:
            if used[prime]:
                continue
            stack.append(prime)
            used[prime] = True
            if backtrack(n+1):
                return True
            used[prime] = False
            stack.pop()
        return False

    backtrack(L)

    return ' '.join(map(str, stack))


def find_divisible(L: int, H: int) -> List[Tuple[int, List[int]]]:
    """각 소수별로 [L..H]구간에서 나눌 수 있는 수가 무엇인지."""
    retval = []
    for prime in primes:
        if prime > H:
            break
        num = L-(L % prime)
        while num < L:
            num += prime
        divisible = []
        while num <= H:
            divisible.append(num)
            num += prime
        if divisible:
            retval.append((prime, divisible))
    return retval


while True:
    L, H = map(int, sys.stdin.readline().split())
    if (L, H) == (0, 0):
        break
    answer = solve(L, H)
    sys.stdout.write(answer+'\n')
