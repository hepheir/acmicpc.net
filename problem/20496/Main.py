# 20496번: Amy, Soup is Salty!

import sys
import collections


MAX_N = 11
MAX_SIMULATION_TIME = (MAX_N ** 2) * 1000

CELL_EMPTY = '.'
CELL_WALL = '#'
CELL_OBSTACLE = '@'
CELL_START = 'S'

DR = (0,  0,  1, -1,)
DC = (1, -1,  0,  0,)

N = int(sys.stdin.readline())
GRID = [[None] * N for _ in range(N)]

queue = collections.deque() # [(r, c)]
should_visit = [[False] * N for _ in range(N)]
should_visit_remaining = 0
curr_visited = [[[] for _ in range(N)] for _ in range(N)] # [(pr, pc, is_straight)]
next_visited = [[[] for _ in range(N)] for _ in range(N)] # [(pr, pc, is_straight)]


def is_empty(r: int, c: int) -> int:
    if not (0 <= r < N and 0 <= c < N):
        return False
    return GRID[r][c] == CELL_EMPTY


def init():
    global should_visit_remaining
    # 최초의 싱크대의 동작
    start_r = None
    start_c = None
    for r in range(N):
        for c, value in enumerate(sys.stdin.readline().strip()):
            GRID[r][c] = value
            if value == CELL_EMPTY:
                should_visit[r][c] = True
                should_visit_remaining += 1
            if value == CELL_START:
                start_c = c
                start_r = r

    # 최초의 소리 진행
    r, c = start_r, start_c
    for dr, dc in zip(DR, DC):
        if not is_empty(r+dr, c+dc):
            continue
        queue.append((r+dr, c+dc))
        next_visited[r+dr][c+dc].append((r, c, False))


def step():
    global should_visit_remaining, next_visited, curr_visited

    def visit(r: int, c: int, nr: int, nc: int, is_straight: bool):
        # 1초뒤, 소리의 위치 방문
        if not next_visited[nr][nc]:
            queue.append((nr, nc))
        next_visited[nr][nc].append((r, c, is_straight))


    def case_3(r: int, c: int):
        pr, pc, is_straight = curr_visited[r][c][0]
        for dr, dc in zip(DR, DC):
            if (r+dr) == pr and (c+dc) == pc:
                # 왔던 방향으로는 안간다.
                continue
            if not is_empty(r+dr, c+dc):
                continue
            # 1초뒤, 소리의 위치 방문
            visit(r, c, r+dr, c+dc, False)

    def case_4(r: int, c: int):
        # 다음 소리의 속도 계산
        dr, dc = 0, 0
        for pr, pc, is_straight in curr_visited[r][c]:
            dr += r-pr
            dc += c-pc
        # 소리가 없어지는 경우들:
        if (dr == 0 and dc == 0):
            return
        if not is_empty(r+dr, c+dc):
            return
        # 1초뒤, 소리의 위치 방문
        visit(r, c, r+dr, c+dc, True)

    def case_5(r: int, c: int):
        pr, pc, is_straight = curr_visited[r][c][0]
        # (4)번 움직임에 의해 직진 중이었을 경우.
        dr = r-pr
        dc = c-pc
        if not is_empty(r+dr, c+dc):
            return
        # 1초뒤, 소리의 위치 방문
        visit(r, c, r+dr, c+dc, True)


    # swap visited
    curr_visited, next_visited = next_visited, curr_visited
    for r in range(N):
        for c in range(N):
            next_visited[r][c].clear()

    for _ in range(len(queue)):
        r, c = queue.popleft()

        # 일단 방문은 했으니 표시.
        if should_visit[r][c]:
            should_visit[r][c] = False
            should_visit_remaining -= 1

        pr, pc, is_straight = curr_visited[r][c][0]
        if len(curr_visited[r][c]) == 1:
            if not is_straight:
                case_3(r, c)
            else:
                case_5(r, c)
        elif len(curr_visited[r][c]) > 1:
            case_4(r, c)


time = 0
init()
while should_visit_remaining > 0:
    if not queue or (time > MAX_SIMULATION_TIME):
        time = -1
        break
    step()
    time += 1

print(time)
