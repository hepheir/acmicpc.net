from functools import cache
import sys

coins: list


@cache
def count_cases(balance: int, unit_idx: int) -> int:
    if unit_idx == 0:
        if balance % coins[unit_idx] == 0:
            return 1
        return 0
    if balance < 0:
        return 0
    cases = 0
    while balance >= 0:
        cases += count_cases(balance, unit_idx-1)
        balance -= coins[unit_idx]
    return cases


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    count_cases.cache_clear()
    sys.stdout.write(f'{count_cases(M, N-1)}\n')
