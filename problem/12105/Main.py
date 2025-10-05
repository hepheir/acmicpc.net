# 12105번: 123456789 찾기

from typing import List

MOD = int(1e9+7)
MAX_N = 10000

# [1..10]의 LCM을 구하고 소인수분해하면
# (2, 2, 2, 3, 3, 5, 7) 이다.
MAX_2 = 3
MAX_3 = 2
MAX_5 = 1
MAX_7 = 1


def count_factor(n: int, f: int) -> int:
    retval = 0
    while n >= f and n % f == 0:
        retval += 1
        n //= f
    return retval


# dp[인덱스 번호][2의 남은 개수][3의 남은 개수][5의 남은 개수][7의 남은 개수]
# 각 소수의 남은 개수를 0으로 만들어야 정답의 조건을 만족하는 경우로 본다.
dp = [[[[[0 for _ in range(MAX_7+1)] for _ in range(MAX_5+1)] for _ in range(MAX_3+1)] for _ in range(MAX_2+1)] for i in range(MAX_N+1)]

# indices: S에서 P를 찾을 수 있는 인덱스 번호 목록
indices = []

P = input().strip()
S = input().strip()
N = len(S)


for i in range(N-len(P)+1):
    if S[i:i+len(P)] == P:
        indices.append(i+1)


dp[0][MAX_2][MAX_3][MAX_5][MAX_7] = 1

for i in range(len(indices)):
    c2 = count_factor(indices[i], 2)
    c3 = count_factor(indices[i], 3)
    c5 = count_factor(indices[i], 5)
    c7 = count_factor(indices[i], 7)
    for p2 in range(MAX_2+1):
        for p3 in range(MAX_3+1):
            for p5 in range(MAX_5+1):
                for p7 in range(MAX_7+1):
                    dp[i+1][p2][p3][p5][p7] += dp[i][p2][p3][p5][p7]
                    dp[i+1][max(p2-c2, 0)][max(p3-c3, 0)][max(p5-c5, 0)][max(p7-c7, 0)] += dp[i][p2][p3][p5][p7]
    for p2 in range(MAX_2+1):
        for p3 in range(MAX_3+1):
            for p5 in range(MAX_5+1):
                for p7 in range(MAX_7+1):
                    dp[i+1][max(p2-c2, 0)][max(p3-c3, 0)][max(p5-c5, 0)][max(p7-c7, 0)] %= MOD

print(dp[len(indices)][0][0][0][0])
