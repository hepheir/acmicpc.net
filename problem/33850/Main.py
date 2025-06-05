# Chill...은 내가 가장 좋아하는 소수

import sys


def is_prime(x: int) -> bool:
    # O(sqrt(x))
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


n, a, b = map(int, sys.stdin.readline().split())
grid = [
    [*map(int, sys.stdin.readline().split())],
    [*map(int, sys.stdin.readline().split())],
]

dp = [0] * n

for i in range(n):
    # i번째 열을 채울 경우

    # 1x2로 채울 때
    dp[i] = max(dp[i], dp[i-1]+(a if is_prime(grid[0][i]+grid[1][i]) else b))

    # 2x1로 채울 때
    if i+1 < n:
        dp[i+1] = max(dp[i+1], dp[i-1] + sum([
            a if is_prime(grid[0][i]+grid[0][i+1]) else b,
            a if is_prime(grid[1][i]+grid[1][i+1]) else b
        ]))

print(dp[n-1])
