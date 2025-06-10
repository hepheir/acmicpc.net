import sys


MAX_R = 100
MAX_H = 100
MAX_C = 100

d = (-1, 0, +1,)

cube = [[[0] * (MAX_C+1) for _ in range(MAX_R+1)] for _ in range(MAX_H+1)]
mine = []

# 입력 받기

R, C, H = map(int, sys.stdin.readline().split())

for h in range(H):
    for r in range(R):
        for c, value in enumerate(sys.stdin.readline().strip()):
            if value == '*':
                mine.append((h, r, c))
                for dh in d:
                    for dr in d:
                        for dc in d:
                            cube[h+dh][r+dr][c+dc] += 1
                            # 우와 6중 for 문...!

# 출력형식에 맞게 처리

for h in range(H):
    for r in range(R):
        for c in range(C):
            cube[h][r][c] = str(cube[h][r][c] % 10)

for h, r, c in mine:
    cube[h][r][c] = '*'


# 출력하기

for h in range(H):
    for r in range(R):
        for c in range(C):
            sys.stdout.write(cube[h][r][c])
        sys.stdout.write('\n')
