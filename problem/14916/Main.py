n = int(input())

cnt_5 = n // 5
n %= 5
if n % 2 and cnt_5:
    n += 5
    cnt_5 -= 1
cnt_2 = n // 2
n %= 2

if not n:
    print(cnt_2+cnt_5)
else:
    print(-1)