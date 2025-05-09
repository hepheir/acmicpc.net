import sys

DX = (-1, 0, 0, 1)
DY = (0, -1, 1, 0)

MAX_W = 20
MAX_H = 20
MAX_MOVES = 10


is_block = [[False] * MAX_H for _ in range(MAX_W)]

while (shape := tuple(map(int, sys.stdin.readline().split()))) != (0, 0):
    w, h = shape
    sx, sy = 0, 0
    ex, ey = 0, 0
    for y in range(h):
        for x, value in enumerate(sys.stdin.readline().split()):
            is_block[x][y] = (value == '1')
            if value == '2':
                sx, sy = x, y
            if value == '3':
                ex, ey = x, y

    def backtracking(x: int, y: int, max_moves: int = MAX_MOVES) -> int:
        min_moves = MAX_MOVES+1
        if max_moves > 0:
            for dx, dy in zip(DX, DY):
                nx, ny = x, y
                did_move = False

                while True:
                    # move stone until ...
                    nx += dx
                    ny += dy

                    # the stone gets out of the board
                    if not (0 <= nx < w and 0 <= ny < h):
                        break

                    # the stone reaches the goal square
                    if (nx, ny) == (ex, ey):
                        return 1

                    # the stone hits a block
                    if is_block[nx][ny]:
                        # check if the stone is blocked immediately
                        if did_move:
                            is_block[nx][ny] = False
                            min_moves = min(
                                min_moves,
                                backtracking(nx-dx, ny-dy, max_moves-1)+1,
                            )
                            is_block[nx][ny] = True
                        break

                    did_move = True
        return min_moves

    if (min_moves := backtracking(sx, sy)) <= MAX_MOVES:
        sys.stdout.write(f'{min_moves}\n')
    else:
        sys.stdout.write('-1\n')
