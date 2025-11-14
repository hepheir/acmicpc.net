from typing import List, Tuple
import sys


MAX_CAPACITY = 100000


def solve(coins: List[Tuple[int, int]], half: int) -> bool:
    if half != int(half):
        return False
    half = int(half)
    dp = [False] * (half+1)
    dp[0] = 1
    for unit, count in coins:
        for i in reversed(range(unit, half+1)):
            if not dp[i-unit]:
                continue
            for j in range(count):
                if i+unit*j > half:
                    break
                dp[i+unit*j] = True
    return dp[half]


for _ in range(3):
    N = int(sys.stdin.readline())
    coins = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    half = sum(unit*count for unit, count in coins) / 2
    if solve(coins, half):
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
