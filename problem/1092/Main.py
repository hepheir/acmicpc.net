# 1092번: 배

import sys
from typing import Dict, List

N = int(sys.stdin.readline())
crane_weight_limits = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
box_weights = list(map(int, sys.stdin.readline().split()))


cranes: Dict[int, List[int]] = {}

for w in crane_weight_limits:
    cranes[w] = []

box_weights.sort()
for w in crane_weight_limits:
    # 박스는 무게에 대해 오름차순 정렬되어 있어, 가벼운 순으로 들어감
    for i in range(M):
        if w >= box_weights[i]:
            cranes[w].append(i)

# 각 크레인 별로 대기열에 박스 번호들이 박스 무게의 오름차순으로 등록되어있다.

box_moved_at = [0] * M
time = 1
crane_weight_limits.sort(reverse=True)
while any(cranes[w] for w in crane_weight_limits):
    for w in crane_weight_limits:
        while cranes[w] and box_moved_at[cranes[w][-1]]:
            cranes[w].pop()
        if cranes[w]:
            box_moved_at[cranes[w].pop()] = time
    time += 1

if all(box_moved_at):
    print(max(box_moved_at))
else:
    print(-1)
