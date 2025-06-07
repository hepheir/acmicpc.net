# 블록의 가장 아랫 부분 높이 편차
BLOCK_MIN_Y = {
    1: [(0,), (0, 0, 0, 0,),],
    2: [(0, 0,),],
    3: [(0, 0, 1,), (1, 0,),],
    4: [(1, 0, 0,), (0, 1,),],
    5: [(0, 0, 0,), (0, 1,), (1, 0, 1,), (1, 0,),],
    6: [(0, 0, 0,), (0, 0,), (0, 1, 1,), (2, 0,),],
    7: [(0, 0, 0,), (0, 2,), (1, 1, 0,), (0, 0,),],
}


C, P = map(int, input().split())
field_h = list(map(int, input().split()))

case_count = 0

for block_h in BLOCK_MIN_Y[P]:
    # 1 <= len(block_h) <= 4
    for c in range(C-len(block_h)+1):
        min_y = max(field_h)
        sum_y = 0
        for dc in range(len(block_h)):
            y = field_h[c+dc] - block_h[dc]
            sum_y += y
            min_y = min(min_y, y)

        # 각 열별로 바닥의 높이 편차와 블록의 높이 편차가 일치하면 +1
        if (sum_y - min_y*len(block_h)) == 0:
            case_count += 1

print(case_count)
