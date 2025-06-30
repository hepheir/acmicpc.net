# 18185번: 라면 사기 (Small)

from typing import List
import sys

INF = sys.maxsize

# 변수 해석:
# A[i]는 i번째 공장에서 사야할 라면의 개수
# B는 지금 라면을 1개 사는 비용
# C는 미리 라면을 1개 사는 비용 으로 보면 될 것 같다.


def solve(A: List[int], B: int, C: int) -> int:
    N = len(A)

    def solve_util(i: int) -> int:
        if i == N:
            return 0
        min_cost = INF
        if i < N-2 and A[i] > 0 and A[i+1] > 0 and A[i+2] > 0:
            A[i] -= 1
            A[i+1] -= 1
            A[i+2] -= 1
            min_cost = min(min_cost, solve_util(i) + 7)
            A[i] += 1
            A[i+1] += 1
            A[i+2] += 1
        if i < N-1 and A[i] > 0 and A[i+1] > 0:
            A[i] -= 1
            A[i+1] -= 1
            min_cost = min(min_cost, solve_util(i) + 5)
            A[i] += 1
            A[i+1] += 1
        if A[i] > 0:
            A[i] -= 1
            min_cost = min(min_cost, solve_util(i) + 3)
            A[i] += 1
        else:
            min_cost = min(min_cost, solve_util(i+1))
        return min_cost
    return solve_util(0)


if __name__ == '__main__':
    N, B, C = int(sys.stdin.readline()), 3, 2
    A = list(map(int, sys.stdin.readline().split()))
    print(solve(A, B, C))
