# 32299번: 게임을 만들어요

import collections

D = ((-1, 0), (0, -1), (0, 1), (1, 0))


def solve(N: int) -> str:
    visited = collections.defaultdict(bool)
    sx = (N+1)//2
    sy = (N+1)//2
    visited[sx, sy] = True
    if can_win(N, sx, sy, visited):
        return 'Hobanwoo'
    else:
        return 'Sangho'


def can_win(N: int, x: int, y: int, visited) -> bool:
    if x == 1 or x == N or y == 1 or y == N:
        return False
    for dx, dy in D:
        if visited[x+dx, y+dy]:
            continue
        visited[x+dx, y+dy] = True
        if not can_win(N, x+dx, y+dy, visited):
            visited[x+dx, y+dy] = False
            return True
        visited[x+dx, y+dy] = False
    return False


if __name__ == '__main__':
    for N in range(3, 33, 2):
        print(N, solve(N))
