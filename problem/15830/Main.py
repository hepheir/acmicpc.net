# 15830번: 싱크홀

from decimal import Decimal

V, W, D = map(int, input().split())

answer = 0
v = Decimal(V)
d = 0
while True:
    t = Decimal(W) / v
    d += (5*t*t)
    if d < D:
        answer += 1
    if d >= D:
        break
    v *= Decimal(8) / 10

print(answer)
