# 2417번: 정수 제곱근

n = int(input())

lo = 0
hi = 1 << 32
while lo < hi:
    mid = (lo+hi)//2
    if mid*mid < n:
        lo = mid+1
    else:
        hi = mid

print(lo)
