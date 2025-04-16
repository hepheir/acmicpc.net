import sys


H, W = map(int, sys.stdin.readline().split())

# prefix sum (2d)
ps = [[0] * (W+1) for _ in range(H+1)]

for y in range(H):
    for x, value in enumerate(map(int, sys.stdin.readline().split())):
        ps[y][x] = value
        ps[y][x] += ps[y-1][x]
        ps[y][x] += ps[y][x-1]
        ps[y][x] -= ps[y-1][x-1]

K = int(sys.stdin.readline())
for _ in range(K):
    i, j, x, y = map(lambda x: int(x)-1, sys.stdin.readline().split())
    sys.stdout.write(f'{ps[x][y] + ps[i-1][j-1] - ps[i-1][y] - ps[x][j-1]}\n')
