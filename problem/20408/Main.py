import sys
import collections


CELL_UNDETREMINED = 0
CELL_BLOCKED = 1
CELL_EMPTY = 2

DC = (0,  1, 0, -1)
DR = (-1, 0, 1,  0)
DIRECTION_NAME = {
    (-1, 0): 'NORTH',
    (1, 0): 'SOUTH',
    (0, -1): 'WEST',
    (0, 1): 'EAST',
}

grid = collections.defaultdict(lambda: CELL_UNDETREMINED)
grid[0, 0] = CELL_EMPTY


def try_move(dr: int, dc: int) -> bool:
    sys.stdout.write(DIRECTION_NAME[(dr, dc)]+'\n')
    sys.stdout.flush()
    return sys.stdin.readline().rstrip() == 'EMPTY'


def dfs(r: int, c: int):
    for dr, dc in DIRECTION_NAME.keys():
        if grid[(r+dr, c+dc)] == CELL_UNDETREMINED:
            if try_move(dr, dc):
                grid[(r+dr, c+dc)] = CELL_EMPTY
                dfs(r+dr, c+dc)
                try_move(-dr, -dc)
            else:
                grid[(r+dr, c+dc)] = CELL_BLOCKED

dfs(0, 0)
sys.stdout.write('DONE\n')
sys.stdout.flush()
sys.exit(0)
