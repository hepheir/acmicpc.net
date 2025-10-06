# 20505번: John's Math Problem

MOD = 998244353

N = input().strip()

pow_2 = [1] * len(N)
pow_11 = [1] * len(N)
for i in range(1, len(N)):
    pow_2[i] = (pow_2[i-1] * 2) % MOD
    pow_11[i] = (pow_11[i-1] * 11) % MOD

answer = 0
for i, n in enumerate(map(int, N)):
    answer += n * pow_2[i] * pow_11[len(N)-1-i]
    answer %= MOD
print(answer)
