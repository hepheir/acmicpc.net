MAX_N = 10000
F = [0] * (MAX_N+1)
F[0] = 0
F[1] = 1

for i in range(2, MAX_N+1):
    F[i] = F[i-1] + F[i-2]


n = int(input())
print(F[n])
