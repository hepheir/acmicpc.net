# 5884번: 감시 카메라

import collections
import sys


N = int(sys.stdin.readline())

node_x = [-1] * N
node_y = [-1] * N

axis_x = collections.defaultdict(list)
axis_x_used = collections.defaultdict(bool)

axis_y = collections.defaultdict(list)
axis_y_used = collections.defaultdict(bool)

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    node_x[i] = x
    node_y[i] = y
    axis_x[x].append(i)
    axis_y[y].append(i)


def solve(i: int = 0, max_depth: int = 3) -> bool:
    if max_depth == 0:
        return all(is_node_visited(j) for j in range(N))

    while i < N and is_node_visited(i):
        i += 1

    if i == N:
        return True

    # i번째 칸에 수직/수평선을 놓아야 함.
    if not axis_x_used[node_x[i]]:
        axis_x_used[node_x[i]] = True
        if solve(i+1, max_depth-1):
            return True
        axis_x_used[node_x[i]] = False

    if not axis_y_used[node_y[i]]:
        axis_y_used[node_y[i]] = True
        if solve(i+1, max_depth-1):
            return True
        axis_y_used[node_y[i]] = False

    return False


def is_node_visited(i: int) -> bool:
    return axis_x_used[node_x[i]] or axis_y_used[node_y[i]]


print(int(solve()))
