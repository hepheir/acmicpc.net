# 30250번: Ones

N = int(input())
M, d = input().split()
M = int(M * int(d))

q = M // N
r = M % N

answer = sum(map(int, str(q)))

if r:
    print('NESIDALO')
else:
    print(answer)
