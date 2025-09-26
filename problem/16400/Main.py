# 16400번: 소수 화폐


MAX_N = 40000
MOD = 123456789

is_prime = [True] * (MAX_N+1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(MAX_N**0.5)+1):
    if not is_prime[i]:
        continue
    for j in range(i*i, MAX_N+1, i):
        is_prime[j] = False

primes = [p for p in range(2, MAX_N+1) if is_prime[p]]

dp = [0] * (MAX_N+1)
dp[0] = 1

for i in primes:
    for j in range(i, MAX_N+1):
        dp[j] += dp[j-i]
        dp[j] %= MOD

N = int(input())
print(dp[N])
