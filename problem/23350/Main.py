# 23350번: K 물류창고

import sys
import collections


def can_be_loaded_over(hi_p: int, hi_w: int, lo_p: int, lo_w: int) -> bool:
    # 우선 순위가 낮거나, 무게가 같거나 가볍다면 적재 가능
    return (lo_p > hi_p) or (lo_w >= hi_w)


N, M = map(int, sys.stdin.readline().split())

rail_queue = collections.deque()
priority_stack = []

for _ in range(N):
    P, W = map(int, sys.stdin.readline().split())
    rail_queue.append((P, W))
    priority_stack.append(P)

# 오름차순 정렬된 우선순위
# (스택처럼 사용하면 큰 수부터 나오게, 뽑아야 할 우선순위 순서대로 역정렬)
priority_stack.sort()


loading_space_stack = []  # (적재 공간) 무게가 높은 순으로 들어가야 함.
other_space = [] # (나머지 공간)

answer = 0
while rail_queue:
    p, w = rail_queue.popleft()

    if p != priority_stack[-1]:
        # 가장 우선 순위가 큰 것이 나올때 까지 rotate
        answer += w
        rail_queue.append((p, w))
        continue

    # 적재 공간에 넣기 위한 과정

    # 재배치가 필요한 것들을 나머지 공간으로 옮김
    while loading_space_stack:
        pl, wl = loading_space_stack.pop()
        if can_be_loaded_over(p, w, pl, wl):
            loading_space_stack.append((pl, wl))
            break
        answer += wl
        other_space.append((pl, wl))

    # 레일에서 내림
    answer += w
    priority_stack.pop()
    loading_space_stack.append((p, w))

    # 나머지 공간에 있던 것들을 적재공간으로 돌러놓음
    while other_space:
        po, wo = other_space.pop()
        answer += wo
        loading_space_stack.append((po, wo))

print(answer)
