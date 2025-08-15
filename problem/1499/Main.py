# 1499번: 뒤집기 수열

import functools

MAX_N = 50
INF = MAX_N+1

A = input().strip()
B = input().strip()
N = len(A)


def r(A: str, i: int, j: int) -> str:
    # O(N)
    A = list(A)
    A[i:j] = reversed(A[i:j])
    return ''.join(A)


def solve() -> int:
    if (ans := min(solve_util(A, lo=0, hi=N), default=INF)) < INF:
        return ans
    else:
        return -1


@functools.cache
def solve_util(A: str, lo: int, hi: int) -> list:
    # O(N^2 x N) = O(N^3)
    answer = []
    if lo == hi:
        answer.append(0)
    else:
        if A[lo] == B[lo]:
            answer.append(min(solve_util(A, lo+1, hi), default=INF))
        if A[hi-1] == B[hi-1]:
            answer.append(min(solve_util(A, lo, hi-1), default=INF))
        A = r(A, lo, hi)
        if A[lo] == B[lo]:
            answer.append(min(solve_util(A, lo+1, hi), default=INF)+1)
        if A[hi-1] == B[hi-1]:
            answer.append(min(solve_util(A, lo, hi-1), default=INF)+1)
    return answer


print(solve())
