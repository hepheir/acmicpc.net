# 30250번: Ones

N = input()
M, d = input().split()

ugne = int('1' * int(N))
jurate = int(d * int(M))

q = ugne // jurate
r = ugne % jurate

answer = sum(map(int, str(q)))

if r:
    print('NESIDALO')
else:
    print(answer)
