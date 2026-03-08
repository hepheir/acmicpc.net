# 4563번: 리벤지 오브 피타고라스

import sys


def solve(A: int) -> int:
    B = A+1
    C = (A*A + B*B)**0.5  # O(A)

    min_diff = 1  # C-B < 1이면 B, C가 자연수를 만족하는 삼각형은 없다.
    max_diff = int(C-B)  # B가 가장 작을 때(B = A+1), C와의 차이가 가장 크다.

    count = 0
    for diff in range(min_diff, max_diff+1):
        # C = B + diff 일 때,
        # A^2 + B^2 = C^2 를 만족하는 B를 구한다.
        B = (A*A - diff*diff) / (2*diff)
        if B.is_integer() and B > 0:
            count += 1
    return count


while (A := int(sys.stdin.readline())) != 0:
    print(solve(A))
