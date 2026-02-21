# 3578번: Holes

h = int(input())

h1 = h % 2
h2 = h // 2

if h1 == 0 and h2 == 0:
    print('1')
elif h1 == 1 and h2 == 0:
    print('0')
else:
    print('4' * (h % 2) + '8' * (h // 2))
