# 33219번: Avant-garde

import math
import sys


n = int(sys.stdin.readline())

blobs = []
for i in range(n):
    x, r = map(int, sys.stdin.readline().split())
    blobs.append((x, r))
blobs.sort()

x_pos = set()
for x, r in blobs:
    x_pos.add(x-r)
    x_pos.add(x)
    x_pos.add(x+r)

# 몇몇의 x좌표에서의 지배원을 구한다.
x_circle = [[x, None] for x in sorted(x_pos)]

for i in range(len(x_circle)):
    max_y = -1
    for j in range(len(blobs)):
        x, r = blobs[j]
        if not (x-r <= x_circle[i][0] <= x+r):
            continue
        y = ((r**2)-(abs(x-x_circle[i][0])**2))**0.5
        if max_y < y:
            max_y = y
            x_circle[i][1] = j

answer = 0
prev_blob = None
for i in range(len(x_circle)):
    x, curr_blob = x_circle[i]
    if prev_blob == curr_blob:
        continue
    cx, cr = blobs[curr_blob]
    answer += math.pi*cr*cr
    if not prev_blob:
        prev_blob = curr_blob
        continue
    px, pr = blobs[prev_blob]
    # 이전 원과 현재 원이 겹치는지 확인.
    if px+pr <= cx-cr:
        continue

    # 교차하는 면적을 구하기 위해 필요한 정보인
    # theta = (교점-원의중심-x축) 내각의 크기를 구한다.
    d = cx-px # 두 원의 거리
    c_theta = math.acos((cr**2 - pr**2 + d**2)/(2*cr*d))
    p_theta = math.acos((pr**2 - cr**2 + d**2)/(2*pr*d))
    h = math.sin(p_theta) * pr

    # 교차하는 면적을 전체 면적에서 제외해준다.
    intersect_area = 0
    intersect_area += pr*pr*p_theta
    intersect_area += cr*cr*c_theta
    intersect_area -= d*h
    answer -= intersect_area

    prev_blob = curr_blob

print(answer)
