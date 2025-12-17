# 3028번: 창영마을

S = input().strip()

has_ball = [True, False, False]

for c in S:
    if c == 'A':
        has_ball[0], has_ball[1] = has_ball[1], has_ball[0]
    if c == 'B':
        has_ball[1], has_ball[2] = has_ball[2], has_ball[1]
    if c == 'C':
        has_ball[0], has_ball[2] = has_ball[2], has_ball[0]

for i in range(3):
    if has_ball[i]:
        print(i + 1)
        break
