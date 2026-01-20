# 9290번: 틱택토 이기기

import sys


grid: list[list[str]] = [[''] * 3 for _ in range(3)]


def solve_testcase(testcase_no: int):
    for y in range(3):
        for x, value in enumerate(sys.stdin.readline().strip()):
            grid[y][x] = value
    value = sys.stdin.readline().strip()
    for y in range(3):
        for x in range(3):
            if grid[y][x] == '-':
                grid[y][x] = value
                if can_win(grid, value):
                    print(f'Case {testcase_no}:')
                    print_grid(grid)
                    return
                grid[y][x] = '-'
    raise AssertionError


def can_win(grid: list[list[str]], value: str) -> bool:
    # 세로로 조건을 만족하는지 검사
    for x in range(3):
        for y in range(3):
            if grid[y][x] != value:
                break
        else:
            return True
    # 가로로 조건을 만족하는지 검사
    for y in range(3):
        for x in range(3):
            if grid[y][x] != value:
                break
        else:
            return True
    # 대각선 아래로 조건을 만족하는지 검사
    for y in range(3):
        x = y
        if grid[y][x] != value:
            break
    else:
        return True
    # 대각선 위로 조건을 만족하는지 검사
    for y in range(3):
        x = 2-y
        if grid[y][x] != value:
            break
    else:
        return True
    return False


def print_grid(grid: list[list[str]]):
    for y in range(3):
        for x in range(3):
            print(grid[y][x], end='')
        print()


T = int(sys.stdin.readline())
for testcase_no in range(1, T+1):
    solve_testcase(testcase_no)
