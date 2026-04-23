# 27297번: 맨해튼에서의 모임

import sys


N, M = map(int, sys.stdin.readline().split())
P = [[] for _ in range(M)]
for i in range(M):
    P[i].extend(map(int, sys.stdin.readline().split()))


# O(M)
def dist(arr: list, x: int) -> int:
    # 점 x로 부터 arr에 있는 모든 점까지의 맨하튼 거리의 합.
    return sum(abs(x-y) for y in arr)


# O(M log X)
def determine_F(i: int) -> int:
    # F_i 를 구한다.
    arr = [p[i] for p in P]
    lo = min(arr)
    hi = max(arr)+1
    while lo < hi:
        mid = lo // 2 + hi // 2
        # Gradient descent 비슷하게.
        if dist(arr, mid) < dist(arr, mid+1):
            hi = mid
        else:
            lo = mid+1
    return lo


# O(NM log X)
F = [determine_F(i) for i in range(N)]

# O(NM)
print(sum(dist([p[i] for p in P], F[i]) for i in range(N)))
print(*F)
