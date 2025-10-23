# 28311번: 벽의 가치

import sys
from collections import deque
from typing import List, Tuple


INF = sys.maxsize

DC = [-1, 1, 0, 0]
DR = [0, 0, -1, 1]


def solve(R: int, C: int, N: int, r: int, c: int, X: List[int], Y: List[int], board: List[List[str]]) -> Tuple[int, int]:
    def iter_pos():
        for r in range(1, R+1):
            for c in range(1, C+1):
                yield r, c

    def inbound(r: int, c: int) -> bool:
        return 0 < r <= R and 0 < c <= C

    def neighbor(r: int, c: int):
        for dr, dc in zip(DR, DC):
            nr, nc = r+dr, c+dc
            if not inbound(nr, nc):
                continue
            yield nr, nc

    def shortest_dist(r: int, c: int, dist: List[List[int]]):
        for x, y in iter_pos():
            dist[x][y] = INF
        queue = deque()
        dist[r][c] = 0
        queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for nr, nc in neighbor(r, c):
                if board[nr][nc] == 'W':
                    continue
                if dist[nr][nc] != INF:
                    continue
                dist[nr][nc] = dist[r][c]+1
                queue.append((nr, nc))

    wall_pos = []
    for x, y in iter_pos():
        if board[x][y] == 'W':
            wall_pos.append((x, y))

    game_score = 0
    wall_game_score = [0] * len(wall_pos) # 각 벽이 없어졌을 때의 게임 점수

    # 벽의 인접칸들에 대한 H에서의 거리 + 2(벽 통과 비용) + 말에서의 거리의 최소 비용을 구해본다.
    # 기존에 H에서 말로 바로 가는 비용보다 저렴하면, 그 경로비용의 차익이 벽의 가치라고 본다.

    dist_from_h = [[0] * (C+1) for _ in range(R+1)]
    shortest_dist(r, c, dist_from_h)

    dist_from_c = [[0] * (C+1) for _ in range(R+1)]
    for component_id in range(N):
        c_r, c_c = X[component_id], Y[component_id]
        old_dist = dist_from_h[c_r][c_c]
        shortest_dist(c_r, c_c, dist_from_c)
        for wall_id in range(len(wall_pos)):
            w_r, w_c = wall_pos[wall_id]
            c2w_dist = min(dist_from_c[r][c] for r, c in neighbor(w_r, w_c))
            h2w_dist = min(dist_from_h[r][c] for r, c in neighbor(w_r, w_c))
            new_dist = min(old_dist, h2w_dist + c2w_dist + 2)
            wall_game_score[wall_id] += new_dist
        game_score += old_dist

    wall_value_sum = 0
    for wall_id in range(len(wall_pos)):
        wall_value = game_score - wall_game_score[wall_id]
        wall_value_sum += wall_value

    return game_score, wall_value_sum


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        R, C, N, r, c = map(int, sys.stdin.readline().split())
        X = [0] * N
        Y = [0] * N
        for i in range(N):
            X[i], Y[i] = map(int, sys.stdin.readline().split())
        board = [[''] * (C+1) for _ in range(R+1)]
        for y in range(1, R+1):
            for x, cell in enumerate(sys.stdin.readline().strip(), start=1):
                board[y][x] = cell
        D, V = solve(R, C, N, r, c, X, Y, board)
        print(D, V)


if __name__ == '__main__':
    main()
