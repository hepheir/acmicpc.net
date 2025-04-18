N = int(input())

for i in reversed(range(N)):
    print(' '*(N-i-1)+'*'*(1+2*i))