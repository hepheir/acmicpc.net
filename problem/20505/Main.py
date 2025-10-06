# 20505번: John's Math Problem

MOD = 998244353

N = input().strip()
answer = 0
for i, n in enumerate(map(int, N)):
    answer += n * pow(2, i, MOD) * pow(11, len(N)-1-i, MOD)
    answer %= MOD
print(answer)
