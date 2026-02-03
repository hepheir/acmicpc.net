# 34726번: DRS

import sys


N, T = map(int, sys.stdin.readline().split())

drivers = []
pos = 0
for _ in range(N):
    D, t = sys.stdin.readline().split()
    pos += int(t)
    pos %= T
    drivers.append((D, pos))

drivers.sort(key=lambda x: x[1])

answer = []
for i in range(N):
    dist = drivers[i][1] - drivers[i-1][1]
    dist += (T if drivers[i-1][1] > drivers[i][1] else 0)
    if 0 < dist <= 1000:
        answer.append(drivers[i][0])
answer.sort()

if not answer:
    print(-1)
else:
    print(' '.join(answer))
