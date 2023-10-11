import sys


# Python의 0.5 반올림 문제 해결용.
def round(f: float):
    i = int(f)
    return i + 1 if (f - i) >= 0.5 else i


n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readlines()))
lst.sort()

thresh = round(n * 0.15)
target = lst[thresh : len(lst)-thresh]

if len(target) == 0:
    print(0)
else:
    print(round(sum(target) / len(target)))