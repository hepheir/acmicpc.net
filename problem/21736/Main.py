import sys

sys.setrecursionlimit(600*600*10)


EMPTY = 'O'
PERSON = 'P'
START = 'I'
VISITED = 'X'

N, M = map(int, sys.stdin.readline().split())
MAP = [list(sys.stdin.readline()) for y in range(N)]

count = 0
sy = 0
sx = 0

def init():
    # Find starting point
    global sy, sx
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == START:
                sy = y
                sx = x
                return


def dfs(y: int, x:int):
    # count people
    global count
    if y < 0 or y >= N or x < 0 or x >= M or MAP[y][x] == VISITED:
        return
    if MAP[y][x] == PERSON:
        count += 1
    MAP[y][x] = VISITED
    dfs(y-1, x)
    dfs(y+1, x)
    dfs(y, x-1)
    dfs(y, x+1)


if __name__ == "__main__":
    init()
    dfs(sy, sx)
    print(count if count > 0 else 'TT')