from typing import *
from collections import defaultdict
import sys


def is_alike(R: int, C: int, A: List[List[int]], B: List[List[int]]) -> bool:
    A_maps = defaultdict(list)
    B_maps = defaultdict(list)
    for r in range(R):
        A_maps[tuple(sorted(A[r]))].append(tuple(A[r]))
        B_maps[tuple(sorted(B[r]))].append(tuple(B[r]))

    for key in A_maps:
        A_maps[key].sort()

    key = min(A_maps)
    row_A = A_maps[key][0]
    for row_B in set(B_maps[key]):
        for colmap_B in generate_colmaps(row_B, row_A):
            for key in A_maps:
                if A_maps[key] != sorted([apply_colmap(row, colmap_B) for row in B_maps[key]]):
                    break
                pass
            else:
                return True
    return False


def generate_colmaps(row_src: Tuple[int], row_dst: Tuple[int]):
    """row_src 를 row_dst 처럼 만들기 위해 각 열 번호가 어떻게 바뀌어야 하는지 매핑."""
    width = len(row_src)
    colmap = list(range(width))
    row_dst = list(row_dst)

    def backtracking(i: int):
        if i == width:
            yield colmap
        else:
            for j in range(i, width):
                if row_src[i] == row_dst[j] and row_src[j] == row_dst[i]:
                    colmap[i], colmap[j] = colmap[j], colmap[i]
                    row_dst[i], row_dst[j] = row_dst[j], row_dst[i]
                    yield from backtracking(i+1)
                    colmap[i], colmap[j] = colmap[j], colmap[i]
                    row_dst[i], row_dst[j] = row_dst[j], row_dst[i]

    return backtracking(0)


def apply_colmap(row: List[int], colmap: List[int]) -> Tuple[int]:
    return tuple([row[colmap[c]] for c in range(len(row))])


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
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')
