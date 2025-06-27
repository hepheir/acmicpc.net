import sys
import datetime


T = int(sys.stdin.readline())
for _ in range(T):
    year, m = map(int, sys.stdin.readline().split())
    date = datetime.datetime(year=year, month=m, day=m) - datetime.timedelta(days=m)
    sys.stdout.write(f'{date.year} {date.month} {date.day}\n')
