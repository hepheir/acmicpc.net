import sys


T_SIZE = 3

def transform(mat: list[list[int]], y: int, x: int):
    for _y in range(y, y+T_SIZE):
        for _x in range(x, x+T_SIZE):
            if mat[_y][_x] == '0':
                mat[_y][_x] = '1'
            else:
                mat[_y][_x] = '0'


N, M = map(int, sys.stdin.readline().split())
A = [list(sys.stdin.readline()) for _ in range(N)]
B = [list(sys.stdin.readline()) for _ in range(N)]

count = 0
for y in range(N-T_SIZE+1):
    for x in range(M-T_SIZE+1):
        if B[y][x] != A[y][x]:
            transform(A, y, x)
            count += 1

for y in range(N):
    for x in range(M):
        if B[y][x] != A[y][x]:
            print('-1')
            exit() # 즉시 종료

print(count)