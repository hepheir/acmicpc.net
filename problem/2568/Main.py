# 2568번: 전깃줄 - 2

from typing import List, Tuple
from bisect import bisect_right
import sys

INF = sys.maxsize


def solve(N: int, L: List[Tuple[int, int]]) -> List[int]:
    L.sort()

    # longest increasing subsequence (length)
    A = [None] + [L[i][1] for i in range(N)]
    D = [0] # Maximum lis length per node
    X = [0] + [INF] * N # Minimum number per length
    XI = [0] * (N+1) # Index of minimum number per length
    P = [None] # Parent/Previous node

    for i in range(1, N+1):
        lis_len = bisect_right(X, A[i])
        D.append(lis_len)
        if X[lis_len] > A[i]:
            X[lis_len] = A[i]
            XI[lis_len] = i
        P.append(XI[lis_len-1])

    # 없애야 하는 전깃줄들의 A 전봇대 번호 집합
    answer = set(L[i][0] for i in range(N))

    lis_len = max(D)
    i = D.index(lis_len)
    while i > 0:
        answer.discard(L[i-1][0])
        i = P[i]

    return [len(answer), *sorted(answer)]


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    L = []
    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
        L.append((a, b))
    for a in solve(N, L):
        sys.stdout.write(f'{a}\n')
