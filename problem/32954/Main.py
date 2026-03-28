# 32954번: 젓가락 고르기

MAX_N = int(1e6)
MAX_A_VALUE = int(1e12)


def clamp(n: int, lo: int, hi: int) -> int:
    return min(max(n, lo), hi)


def to_odd(n: int) -> int:
    """n보다 작거나 같은 가장 큰 홀수"""
    return n if n % 2 == 1 else n-1


def to_even(n: int) -> int:
    """n보다 작거나 같은 가장 큰 짝수"""
    return n-1 if n % 2 == 1 else n


N, K = map(int, input().split())
A = sorted(map(int, input().split()))
a = [0] * N


def get_min_k(x: int) -> int:
    """x개의 젓가락으로 만들 수 있는 가장 작은 쌍의 개수"""
    for i in range(N):
        a[i] = A[i]

    for i in range(N):
        if x == 0:
            break
        diff = clamp(to_odd(x // (N-i)), 0, to_odd(a[i]))
        x -= diff
        a[i] -= diff

    for i in range(N):
        if x == 0:
            break
        diff = clamp(to_even(x), 0, to_even(a[i]))
        x -= diff
        a[i] -= diff

    for i in range(N):
        if x == 0:
            break
        diff = min(a[i], x)
        a[i] -= diff
        x -= diff

    return sum((A[i] - a[i]) // 2 for i in range(N))


lo = 0
hi = MAX_N * MAX_A_VALUE

while lo < hi:
    mid = (lo + hi) // 2
    if get_min_k(mid) < K:
        lo = mid + 1
    else:
        hi = mid

if get_min_k(lo) == K:
    print(lo)
else:
    print(-1)
