# 5884번: 감시 카메라

import collections
import sys


N = int(sys.stdin.readline())

X = [-1] * N
Y = [-1] * N
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    X[i] = x
    Y[i] = y


x_counter = collections.defaultdict(int)
y_counter = collections.defaultdict(int)


def solve(max_depth: int = 3) -> bool:
    if max_depth == 0:
        for x, y in zip(X, Y):
            if x_counter[x] == 0 and y_counter[y] == 0:
                return False
        return True

    for x, y in zip(X, Y):
        if x_counter[x] > 0 or y_counter[y] > 0:
            continue
        x_counter[x] += 1
        y_counter[y] += 1
        if solve(max_depth-1):
            return True
        x_counter[x] -= 1
        y_counter[y] -= 1

    return False


print(int(solve()))
