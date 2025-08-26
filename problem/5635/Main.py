# 5635번: 생일

import datetime
import sys


people = []

n = int(sys.stdin.readline())
for _ in range(n):
    name, dd, mm, yy = sys.stdin.readline().split()
    date = datetime.date(year=int(yy), month=int(mm), day=int(dd))
    people.append((date, name))

print(max(people)[1])
print(min(people)[1])
