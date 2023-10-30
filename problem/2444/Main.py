N = int(input())

for i in range(N):
    print(' '*(N-i-1)+'*'*(1+2*i))
for i in reversed(range(N-1)):
    print(' '*(N-i-1)+'*'*(1+2*i))