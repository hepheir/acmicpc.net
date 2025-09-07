# 16490번: 외계인의 침투

import math

DEG_30 = math.pi/6


a, t = map(int, input().split())

# 원의 중심이 원점 O(0, 0)에 있고, 점 A는 y축 위 양의 방향에 있다고 하자.
# 이 때, r은 원의 반지름 길이이다.

r = t/2/math.cos(DEG_30)

O = (0, 0)
A = (0, +r)
B = (-r*math.cos(DEG_30), -r*math.sin(DEG_30))
C = (+r*math.cos(DEG_30), -r*math.sin(DEG_30))


OAP_radian = math.acos(a/(2*r))
P = (a*math.sin(OAP_radian), A[1]-a*math.cos(OAP_radian))

b = math.hypot(B[0]-P[0], B[1]-P[1])
c = math.hypot(C[0]-P[0], C[1]-P[1])

print(f'{b*c:.0f}')  # Python에서 올바르게 반올림하기.
