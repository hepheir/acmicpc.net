# 12199번: Password Attacker (Large)

import sys
import functools
import math

MOD = int(1e9+7)


@functools.cache
def solve(M: int, N: int) -> int:
    # M개의 숫자로 길이 N의 비밀번호를 만드는 경우의 수
    if M == 1:
        return 1
    answer = 0
    for count in range(1, N-(M-1)+1):
        answer += math.comb(N, count) * solve(M-1, N-count)
    return answer % MOD


T = int(sys.stdin.readline())
for t in range(1, T+1):
    M, N = map(int, sys.stdin.readline().split())
    answer = solve(M, N)
    sys.stdout.write(f'Case #{t}: {answer}\n')