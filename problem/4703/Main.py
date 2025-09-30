# 4703번: 그림의 추측

from collections import defaultdict
from typing import List
import sys


MAX_H = int(1e10)
MAX_PRIME = int(MAX_H**0.5)


is_prime = [True] * (MAX_PRIME+1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, MAX_PRIME+1):
    if not is_prime[i]:
        continue
    for j in range(i*i, MAX_PRIME+1, i):
        is_prime[j] = False

primes = [i for i in range(2, MAX_PRIME+1) if is_prime[i]]


def get_prime_factors(n: int) -> List[int]:
    retval = []
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            retval.append(p)
            while n % p == 0:
                n //= p
    if n > 1:
        retval.append(n)
    return retval


def solve(L: int, H: int) -> str:
    prime_matched_to = defaultdict(int)
    prime_visited = defaultdict(bool)
    prime_visited_all_time = set()

    def bipartite_matching(n: int) -> bool:
        for p in get_prime_factors(n):
            if prime_visited[p]:
                continue
            prime_visited[p] = True
            if prime_matched_to[p] == 0 or bipartite_matching(prime_matched_to[p]):
                prime_matched_to[p] = n
                return True
        return False

    for n in reversed(range(L, H+1)):
        prime_visited.clear()
        assert bipartite_matching(n)
        prime_visited_all_time.update(p for p in prime_visited if prime_visited[p])

    number_matched_to = {prime_matched_to[p]: p for p in prime_visited_all_time}
    return ' '.join(map(str, [number_matched_to[n] for n in range(L, H+1)]))


while True:
    L, H = map(int, sys.stdin.readline().split())
    if (L, H) == (0, 0):
        break
    answer = solve(L, H)
    sys.stdout.write(answer+'\n')
