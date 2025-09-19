# 12583번: Rotate (Small)

import sys


MAX_N = 7
BUFFER = [[None] * MAX_N for _ in range(MAX_N)]


def solve(N: int, K: int, grid: list) -> str:
    rotate(N, grid)
    gravity(N, grid)
    return winner(N, K, grid)


def rotate(N: int, grid: list):
    for y in range(N):
        for x in range(N):
            BUFFER[x][N-1-y] = grid[y][x]
    for y in range(N):
        for x in range(N):
            grid[y][x] = BUFFER[y][x]


def gravity(N: int, grid: list):
    for x in range(N):
        y_dst = N-1
        for y_src in range(N-1, -1, -1):
            if grid[y_src][x] != '.':
                value = grid[y_src][x]
                grid[y_src][x] = '.'
                grid[y_dst][x] = value
                y_dst -= 1


def winner(N: int, K: int, grid: list) -> str:
    R_win = False
    B_win = False
    # check horizontal
    for y in range(N):
        r, b = check_row(grid[y])
        R_win |= r
        B_win |= b

    # check vertical
    for x in range(N):
        r, b = check_row([grid[y][x] for y in range(N)])
        R_win |= r
        B_win |= b

    # check diagonal
    for x in range(-N, 2*N):
        r, b = check_row([grid[y][x-y] for y in range(N) if 0 <= (x-y) < N])
        R_win |= r
        B_win |= b

        r, b = check_row([grid[y][x+y] for y in range(N) if 0 <= (x+y) < N])
        R_win |= r
        B_win |= b

    if R_win and B_win:
        return 'Both'
    if R_win:
        return 'Red'
    if B_win:
        return 'Blue'
    return 'Neither'


def check_row(row: list) -> tuple:
    R_win = False
    B_win = False
    count = 0
    last = None
    for curr in row:
        if curr != last:
            count = 1
            last = curr
            continue
        count += 1
        if count >= K and last == 'R':
            R_win = True
        if count >= K and last == 'B':
            B_win = True
    return R_win, B_win




T = int(sys.stdin.readline())
for x in range(1, T+1):
    N, K = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    y = solve(N, K, grid)
    sys.stdout.write(f'Case #{x}: {y}\n')
