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
curr_visited = [[[] for _ in range(N)] for _ in range(N)] # [(pr, pc)]
next_visited = [[[] for _ in range(N)] for _ in range(N)] # [(pr, pc)]


def is_empty(r: int, c: int) -> int:
    if not (0 <= r < N and 0 <= c < N):
        return False
    return GRID[r][c] == CELL_EMPTY


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
    if not next_visited[r+dr][c+dc]:
        queue.append((r+dr, c+dc))
    next_visited[r+dr][c+dc].append((r, c))


def simulate() -> int:
    global should_visit_remaining, next_visited, curr_visited
    if should_visit_remaining == 0:
        return 0
    for time in range(1, MAX_SIMULATION_TIME):
        curr_visited, next_visited = next_visited, curr_visited
        for r in range(N):
            for c in range(N):
                next_visited[r][c].clear()
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if should_visit[r][c]:
                should_visit[r][c] = False
                should_visit_remaining -= 1
            # 여러 소리가 부딫혔을 때.
            if len(curr_visited[r][c]) > 1:
                # 다음 소리의 속도 계산
                dr, dc = 0, 0
                for i in range(len(curr_visited[r][c])):
                    pr, pc = curr_visited[r][c][i]
                    dr += r-pr
                    dc += c-pc
                # 소리가 없어지는 경우들:
                if (dr == 0 and dc == 0):
                    continue
                if not is_empty(r+dr, c+dc):
                    continue
                # 1초뒤, 소리의 위치 방문
                if not next_visited[r+dr][c+dc]:
                    queue.append((r+dr, c+dc))
                next_visited[r+dr][c+dc].append((r, c))
                continue
            # 하나의 소리만 있을 때.
            pr, pc = curr_visited[r][c][0]
            velocity = max(abs(r-pr), abs(c-pc))
            dr_0, dc_0 = (r-pr)//velocity, (c-pc)//velocity
            for dr, dc in zip(DR, DC):
                if dr == -dr_0 and dc == -dc_0:
                    # 왔던 방향으로는 안간다.
                    continue
                if not is_empty(r+dr, c+dc):
                    continue
                # 1초뒤, 소리의 위치 방문
                if not next_visited[r+dr][c+dc]:
                    queue.append((r+dr, c+dc))
                next_visited[r+dr][c+dc].append((r, c))

        if should_visit_remaining == 0:
            # 모든 빈 격자에 도달함.
            return time
        if not queue:
            # 모든 빈 격자에 도달하지 못한 채 소리가 전부 사라짐.
            return -1

    # 시뮬레이션 최대 횟수 초과.
    return -1


print(simulate())
