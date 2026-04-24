# 13325번: 이진 트리

import collections
import sys


def complete_binary_tree_size(height: int) -> int:
    if height < 0:
        return 0
    return 1 + 2 * complete_binary_tree_size(height-1)


k = int(sys.stdin.readline())
P = [0, *map(int, sys.stdin.readline().split())] # 각 노드로 가기 위한 부모로 부터의 가중치
D = [0] * complete_binary_tree_size(k)

leaf_start = complete_binary_tree_size(k-1)
leaf_end = complete_binary_tree_size(k)

queue = collections.deque(range(leaf_start, leaf_end))

while len(queue) > 1:
    l = queue.popleft()
    r = queue.popleft()
    p = l >> 1

    ld = D[l]+P[l]
    rd = D[r]+P[r]

    if ld < rd:
        P[l] += rd-ld
    else:
        P[r] += ld-rd

    D[p] = max(ld, rd)

    queue.append(p)

print(sum(P))
