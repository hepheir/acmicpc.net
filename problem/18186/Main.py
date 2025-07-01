# 18186번: 라면 사기 (Large)

from typing import List
import sys

INF = sys.maxsize

N, B, C = map(int, sys.stdin.readline().split())
A = [*map(int, sys.stdin.readline().split()), 0, 0]


def solve(A: List[int], B: int, C: int) -> int:
    SUM_A = sum(A)
    if B < C:
        return B * SUM_A
    cost = 0
    for i in reversed(range(len(A))):
        # at B+2C cost
        if A[i-2] < A[i-1]:
            amount = min(A[i-1] - A[i-2], A[i])
            A[i] -= amount
            A[i-1] -= amount
            cost += (B+C) * amount
        amount = min(A[i], A[i-1], A[i-2])
        A[i] -= amount
        A[i-1] -= amount
        A[i-2] -= amount
        cost += (B+2*C) * amount
        # at B+C cost
        amount = min(A[i-1], A[i])
        A[i] -= amount
        A[i-1] -= amount
        cost += (B+C) * amount
        # at B cost
        amount = A[i]
        A[i] -= amount
        cost += B * amount
    return cost


print(solve(A, B, C))
