import sys


MAX_N = 20

B: list[int] = [0] * (1 << MAX_N)

X, Y, Z = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

for i in range(N):
    B[i] = int(sys.stdin.readline().split()[1])

ans = 0


def solve(i: int = MAX_N, x: int = 0, y: int = 0, z: int = 0) -> int:
    global ans
    size = 1 << i
    if x >= X or y >= Y or z >= Z:
        return
    elif B[i] > 0 and (x+size) <= X and (y+size) <= Y and (z+size) <= Z:
        B[i] -= 1
        ans += 1
        return
    elif i == 0:
        raise ValueError()
    else:
        i -= 1
        size = 1 << i
        solve(i, x, y, z)
        solve(i, x, y, z+size)
        solve(i, x, y+size, z)
        solve(i, x, y+size, z+size)
        solve(i, x+size, y, z)
        solve(i, x+size, y, z+size)
        solve(i, x+size, y+size, z)
        solve(i, x+size, y+size, z+size)


try:
    solve()
except ValueError:
    ans = -1
finally:
    print(ans)
