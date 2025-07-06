# 33384번: Except One

import sys


def solve(p: int, k: int, t: int) -> int:
    dp = [0] * (t+1)
    # 곱해서 0이 되어 사라지면 안되니까 예외적으로 1 부여.
    # (어차피 1 <= t여서 dp[0]이 조회될 일은 없음.)
    dp[0] = 1
    for number in range(1, p):
        if number == k:
            continue
        for i in reversed(range(t)):
            dp[i+1] = (dp[i+1] + dp[i] * number) % p
    return dp[t]



if __name__ == "__main__":
    p, k, t = map(int, sys.stdin.readline().split())
    answer = solve(p, k, t)
    print(answer)
