# 15788번: 밸런스 스톤

import sys


N = int(sys.stdin.readline())
puzzle = [[0] * N for _ in range(N)]
empty_x, empty_y = 0, 0
for y in range(N):
    for x, val in enumerate(map(int, sys.stdin.readline().split())):
        puzzle[y][x] = val
        if val == 0:
            empty_x, empty_y = x, y

def solve() -> int:
    std_sum = sum(puzzle[0] if empty_y != 0 else puzzle[1])
    M = std_sum - sum(puzzle[empty_y])
    puzzle[empty_y][empty_x] = M
    # 규칙 1 검사 (가로)
    for y in range(N):
        cur_sum = 0
        for x in range(N):
            cur_sum += puzzle[y][x]
        if cur_sum != std_sum:
            return -1
    # 규칙 2 검사 (세로)
    for x in range(N):
        cur_sum = 0
        for y in range(N):
            cur_sum += puzzle[y][x]
        if cur_sum != std_sum:
            return -1
    # 규칙 3 검사 (대각)
    cur_sum = 0
    for x, y in zip(range(N), range(N)):
        cur_sum += puzzle[y][x]
    if cur_sum != std_sum:
        return -1
    cur_sum = 0
    for x, y in zip(range(N), reversed(range(N))):
        cur_sum += puzzle[y][x]
    if cur_sum != std_sum:
        return -1
    return M


print(solve())
