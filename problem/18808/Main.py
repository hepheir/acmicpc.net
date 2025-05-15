import sys

MAX_H = 40
MAX_W = 40
MAX_R = 10
MAX_C = 10

EMPTY = '0'
FILLED = '1'


H, W, K = map(int, sys.stdin.readline().split())
R, C = 0, 0

notebook = [[EMPTY] * MAX_H for _ in range(MAX_W)]
sticker = [[EMPTY] * MAX_R for _ in range(MAX_C)]
sticker_buffer = [[EMPTY] * MAX_R for _ in range(MAX_C)]


def is_placable(x: int, y: int) -> bool:
    for dy in range(R):
        for dx in range(C):
            if sticker[dx][dy] == FILLED and notebook[x+dx][y+dy] == FILLED:
                return False
    return True


def place(x: int, y: int):
    for dy in range(R):
        for dx in range(C):
            if sticker[dx][dy] == FILLED:
                notebook[x+dx][y+dy] = FILLED


def rotate():
    global R, C, sticker, sticker_buffer
    for sy in range(R):
        for sx in range(C):
            ex = R-1-sy
            ey = sx
            sticker_buffer[ex][ey] = sticker[sx][sy]
    sticker, sticker_buffer = sticker_buffer, sticker
    R, C = C, R


def try_place():
    for _ in range(4):
        for y in range(H-R+1):
            for x in range(W-C+1):
                if is_placable(x, y):
                    place(x, y)
                    return
        rotate()



for _ in range(K):
    R, C = map(int, sys.stdin.readline().split())
    is_placed = False
    for y in range(R):
        for x, val in enumerate(sys.stdin.readline().split()):
            sticker[x][y] = val
    try_place()

filled_count = 0
for y in range(H):
    for x in range(W):
        if notebook[x][y] == FILLED:
            filled_count += 1

print(filled_count)
