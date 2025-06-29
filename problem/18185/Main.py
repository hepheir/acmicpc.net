# 18185번: 라면 사기 (Small)

from typing import List
import sys

INF = sys.maxsize

N, B, C = int(sys.stdin.readline()), 3, 2
A = list(map(int, sys.stdin.readline().split()))

# 변수 해석:
# A[i]는 i번째 공장에서 사야할 라면의 개수
# B는 지금 라면을 1개 사는 비용
# C는 미리 라면을 1개 사는 비용 으로 보면 될 것 같다.


def solve(A: List[int], B: int, C: int) -> int:
    SUM_A = sum(A)
    if B < C:
        return B * SUM_A
    cost = 0
    for i in reversed(range(len(A))):
        if i-2 >= 0:
            amount = min(A[i], A[i-1], A[i-2])
            A[i] -= amount
            A[i-1] -= amount
            A[i-2] -= amount
            cost += (B+2*C) * amount
        if i-1 >= 0:
            amount = min(A[i], A[i-1])
            A[i] -= amount
            A[i-1] -= amount
            cost += (B+C) * amount
        amount = A[i]
        A[i] -= amount
        cost += B * amount
    return cost


print(solve(A, B, C))
