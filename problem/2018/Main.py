# 2018번: 수들의 합 5


N = int(input())


def range_sum(s: int, e: int) -> int:
    return (e-s+1)*(s+e)//2


answer = 0
for s in range(1, N+1):
    lo = s
    hi = N
    while lo < hi:
        mid = (lo+hi)//2
        if range_sum(s, mid) < N:
            lo = mid+1
        else:
            hi = mid
    if range_sum(s, lo) == N:
        answer += 1

print(answer)
