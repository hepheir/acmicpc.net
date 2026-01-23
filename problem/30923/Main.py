# 30923번: 크냑과 3D 프린터

N = int(input())
h = list(map(int, input().split()))

area = 0
prev_h = 0
for i in range(N):
    curr_h = h[i]
    dh = abs(prev_h-curr_h)
    area += 2*(1+curr_h)+dh
    prev_h = curr_h
area += h[-1]

print(area)
