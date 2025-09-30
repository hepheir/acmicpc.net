# 4703번: 그림의 추측

from collections import defaultdict
from typing import List
import sys


MAX_PRIME = int(1e5)

is_prime = [True] * (MAX_PRIME+1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, MAX_PRIME+1):
    if not is_prime[i]:
        continue
    for j in range(i*i, MAX_PRIME+1, i):
        is_prime[j] = False

PRIMES = [i for i in range(2, MAX_PRIME+1) if is_prime[i]]


def get_prime_factors(n: int) -> List[int]:
    retval = []
    for p in PRIMES:
        if n % p == 0:
            retval.append(p)
            while n % p == 0:
                n //= p
        if n == 1:
            break
    if n > 1:
        retval.append(n)
    return retval


def solve(L: int, H: int) -> str:
    solved = False
    used = defaultdict(bool)
    factors = dict()
    factor_count = defaultdict(int)
    prime_matched = defaultdict(int)
    answer = None

    for n in range(L, H+1):
        factors[n] = get_prime_factors(n)
        factor_count[n] = len(factors[n])

    def find_next_number_to_allocate() -> int:
        n = 0
        for i in range(L, H+1):
            if (prime_matched[i] == 0) and (n == 0 or factor_count[i] == 1):
                n = i
        return n

    def assign(amount: int = H-L+1):
        nonlocal solved, answer
        if solved:
            return

        if amount == 0:
            solved = True
            answer = ' '.join(map(str, [prime_matched[n] for n in range(L, H+1)]))
            return

        amount -= 1

        n = find_next_number_to_allocate()
        prime_matched[n] = -1

        for p in factors[n]:
            if used[p]:
                continue

            failed = False
            for i in range(L, H+1):
                if (prime_matched[i] == 0) and (p in factors[i]):
                    factor_count[i] -= 1
                    if factor_count[i] == 0:
                        failed = True

            if not failed:
                prime_matched[n] = p
                used[p] = True
                assign(amount)
                if solved:
                    return
                used[p] = False

            for i in range(L, H+1):
                if (prime_matched[i] == 0) and (p in factors[i]):
                    factor_count[i] += 1

        prime_matched[n] = 0
        return

    assign()
    assert answer is not None
    return answer


while True:
    L, H = map(int, sys.stdin.readline().split())
    if (L, H) == (0, 0):
        break
    answer = solve(L, H)
    sys.stdout.write(answer+'\n')
