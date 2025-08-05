# 15015번: Manhattan Mornings

from typing import Tuple, List
from bisect import bisect_right
import sys

INF = sys.maxsize


n = int(sys.stdin.readline())
x_h, y_h, x_w, y_w = map(int, sys.stdin.readline().split())
nodes: List[Tuple[int, int]] = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    nodes.append((x, y))


# 심부름을 처리할 수 있는 경계 범위
x_min, x_max = min(x_h, x_w), max(x_w, x_h)
y_min, y_max = min(y_h, y_w), max(y_w, y_h)

# x_min -> x_max 방향으로 이동할 때, y값의 증감 여부
y_asc = True if ((x_h-x_w)*(y_h-y_w)) >= 0 else False


# LIS, O(n log n)
# 변수명 조합 A, D, X 는 다음 문서를 참고함:
# https://namu.wiki/w/최장%20증가%20부분%20수열#s-3.1
A = [(-INF, -INF)]
for x, y in nodes:
    if x_min <= x <= x_max and y_min <= y <= y_max:
        # x = [x_min, x_max] 구간에 대한 LIS 문제로 치환하기 위해,
        # y도 증가하는 방향으로 맞춰준다.
        A.append((x, y if y_asc else -y))
A.sort()

N = len(A)
D = [0] * N
X = [INF] * N
X[0] = -INF

# y에 대한 LIS의 길이를 탐색한다.
for i in range(1, N):
    y = A[i][1]
    D[i] = bisect_right(X, y, lo=0, hi=i)
    X[D[i]] = min(X[D[i]], y)


answer = max(D)
print(answer)
