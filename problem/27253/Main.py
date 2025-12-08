# 27253번: Конфеты для первоклассников

n = int(input())
a = int(input())
b = int(input())

andrey = b
anya = b

anya = max(anya - (andrey + anya) % n, a)
andrey = max(andrey - (andrey + anya) % n, a)

print(andrey, anya)
