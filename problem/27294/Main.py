# 27294번: 몇개고?

T, S = map(int, input().split())

if 12 <= T <= 16 and S == 0:
    count = 320
else:
    count = 280

print(count)
