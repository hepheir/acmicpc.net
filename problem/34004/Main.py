import math
import sys

INF = sys.maxsize

"""Concept:

최대한 직육면체에 맞춰준다.

(1) 정육면체가 표면적이 가장 적으므로, 정육면체를 먼저 만들고,
(2) 최대한 많은 면에 접할 수 있도록 블록들을 붙여가며 표면적이 가장 적은 직육면체를 만들어 나아간다. O(정육면체 변의 길이)
(3) 남은 블록은 직육면체의 가장 넓은 면에 적절히 붙여준다. O(직육면체 가장 긴 변의 길이)

O(정육면체 변의 길이) = N의 세제곱근
"""


def solve(blocks: int) -> int:
    r = int(blocks ** (1/3))
    edges = [r, r, r]
    while True:
        edges.sort()
        if blocks < (edges[0]+1)*edges[1]*edges[2]:
            break
        edges[0] += 1
    area = 2*(edges[0]*edges[1]+edges[1]*edges[2]+edges[2]*edges[0])
    blocks -= edges[0]*edges[1]*edges[2]
    if blocks > 0:
        min_y = math.ceil(blocks / edges[2])
        max_y = edges[1]
        min_area_diff = INF
        for y in range(min_y, max_y+1):
            x = math.ceil(blocks / y)
            area_diff = 2*(x+y)
            if min_area_diff > area_diff:
                min_area_diff = area_diff
        area += min_area_diff
    return area


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    answer = solve(N)
    sys.stdout.write(f'{answer}\n')