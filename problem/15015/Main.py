# 15015번: Man

import sys



n = int(sys.stdin.readline())
xh, yh, xw, yw = map(int, sys.stdin.readline().split())

# 집과 직장을 포함하여 방문가능한 좌표들 모음.
nodes = [(xh, yh), (xw, yw)]

x_min = min(nodes[0][0], nodes[-1][0])
x_max = max(nodes[0][0], nodes[-1][0])
y_min = min(nodes[0][1], nodes[-1][1])
y_max = max(nodes[0][1], nodes[-1][1])

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x_min <= x <= x_max and y_min <= y <= y_max:
        nodes.append((x, y))

nodes.sort()


def max_visitable_nodes(i: int, j: int) -> int:
    """i, j번째 노드를 방문할 때, [i+1:j-1] 구간에 존재하며
    총 이동 거리를 늘리지 않으면서 방문 가능한 노드의 개수.
    """
    x_min = min(nodes[i][0], nodes[j][0])
    x_max = max(nodes[i][0], nodes[j][0])
    y_min = min(nodes[i][1], nodes[j][1])
    y_max = max(nodes[i][1], nodes[j][1])
    max_count = 0
    for k in range(i+1, j):
        x, y = nodes[k]
        if x_min <= x <= x_max and y_min <= y <= y_max:
            count = 1 + max_visitable_nodes(i, k) + max_visitable_nodes(k, j)
            max_count = max(max_count, count)
    return max_count


answer = max_visitable_nodes(0, len(nodes)-1)
print(answer)
