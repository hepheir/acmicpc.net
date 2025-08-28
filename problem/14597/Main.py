# 14597번: Quilting (Large)

from functools import cache
import sys

H, W = map(int, sys.stdin.readline().split())
B1 = []
B2 = []

for _ in range(H):
    B1.append(list(map(int, sys.stdin.readline().split())))

for _ in range(H):
    B2.append(list(map(int, sys.stdin.readline().split())))


@cache
def find_min_E(y: int, x: int) -> int:
    if y == H:
        return 0

    if not (0 <= x < W):
        return sys.maxsize

    return (B1[y][x]-B2[y][x])**2 + min(
        find_min_E(y+1, x-1),
        find_min_E(y+1, x),
        find_min_E(y+1, x+1),
    )


def solve() -> int:
    return min(find_min_E(0, x) for x in range(W))


print(solve())
