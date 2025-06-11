from typing import *
from collections import defaultdict
import sys


def is_alike(R: int, C: int, A: List[List[int]], B: List[List[int]]) -> bool:
    A_maps = defaultdict(int)
    B_maps = defaultdict(int)

    A_maps.clear()
    B_maps.clear()
    for r in range(R):
        A_maps[tuple(sorted([A[r][c] for c in range(C)]))] += 1
        B_maps[tuple(sorted([B[r][c] for c in range(C)]))] += 1
    for key in A_maps:
        if A_maps[key] != B_maps[key]:
            return False

    A_maps.clear()
    B_maps.clear()
    for c in range(C):
        A_maps[tuple(sorted([A[r][c] for r in range(R)]))] += 1
        B_maps[tuple(sorted([B[r][c] for r in range(R)]))] += 1
    for key in A_maps:
        if A_maps[key] != B_maps[key]:
            return False

    return True


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        A = [[0] * m for _ in range(n)]
        B = [[0] * m for _ in range(n)]
        for r in range(n):
            for c, value in enumerate(map(int, sys.stdin.readline().split())):
                A[r][c] = value
        for r in range(n):
            for c, value in enumerate(map(int, sys.stdin.readline().split())):
                B[r][c] = value

        if is_alike(n, m, A, B):
            sys.stdout.write('TAK\n')
        else:
            sys.stdout.write('NIE\n')
