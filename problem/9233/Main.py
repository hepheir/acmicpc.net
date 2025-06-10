from typing import *

import math
import sys


class InvalidMoleculeException(Exception):
    pass


MAX_R = 5
MAX_C = 5

DR = (-1, 0, 0, 1,)
DC = (0, -1, 1, 0,)

GRID = [[None] * MAX_C for _ in range(MAX_R)]
BOND = [[0] * MAX_C for _ in range(MAX_R)]
BOND_CNT_ASC = '.HONC'


def init_bond(R: int, C: int, grid: List[List[str]]) -> List[List[int]]:
    for r in range(R):
        for c in range(C):
            BOND[r][c] = BOND_CNT_ASC.index(grid[r][c])
    return BOND


def preproc_bond(R: int, C: int, bond: List[List[int]]):
    # inplace = True
    # 확실하게 놔야할 것은 놔버린다.
    has_changed = True
    while has_changed:
        has_changed = False
        for r in range(R):
            for c in range(C):
                if bond[r][c] == 0:
                    continue

                n = 0 # 연결 가능한 인접 원자의 수
                k = bond[r][c]
                for dr, dc in zip(DR, DC):
                    if not (0 <= r+dr < R and 0 <= c+dc < C):
                        continue
                    if bond[r+dr][c+dc] == 0:
                        continue
                    n += 1

                comb = math.comb(n, k) # 이 원소가 인접한 원소와 연결되는 경우의 수.
                if comb == 0:
                    # 다른 원소와 연결해야 하나, 연결 가능한 원소가 없음.
                    raise InvalidMoleculeException
                if comb == 1:
                    # 선택지가 없이 연결해야할 대상이 결정적임.
                    for dr, dc in zip(DR, DC):
                        if not (0 <= r+dr < R and 0 <= c+dc < C):
                            continue
                        if bond[r+dr][c+dc] > 0:
                            bond[r+dr][c+dc] -= 1
                            bond[r][c] -= 1
                    has_changed = True
    return bond


def list_edges(R: int, C: int, bond: List[List[int]]) -> List[Tuple[int, int, int, int]]:
    edge = []
    for r in range(R):
        for c in range(C):
            if bond[r][c] == 0:
                continue
            for dr, dc in zip(DR[:2], DC[:2]):
                if not (0 <= r+dr < R and 0 <= c+dc < C):
                    continue
                if bond[r+dr][c+dc] == 0:
                    continue
                edge.append((r, c, r+dr, c+dc))
    return edge


def count_total_bonds(R: int, C: int, bond: List[List[int]]) -> int:
    total_bond_count = 0
    for r in range(R):
        for c in range(C):
            total_bond_count += bond[r][c]
    if total_bond_count % 2 == 1:
        raise InvalidMoleculeException
    return total_bond_count // 2


def validate(R: int, C: int, grid: List[List[str]]) -> bool:
    bond = init_bond(R, C, grid)
    bond = preproc_bond(R, C, bond)
    edge = list_edges(R, C, bond) # len(edge) <= 40
    total_bond_count = count_total_bonds(R, C, bond)

    def backtracking(i: int = 0, bond_count: int = 0) -> bool:
        if len(edge) - i < total_bond_count - bond_count:
            return False
        if i == len(edge):
            return True

        # don't choose this edge
        if backtracking(i+1, bond_count):
            return True

        # choose this edge
        r0, c0, r1, c1 = edge[i]
        bond[r0][c0] -= 1
        bond[r1][c1] -= 1
        if bond[r0][c0] >= 0 and bond[r1][c1] >= 0 and backtracking(i+1, bond_count+1):
            return True
        bond[r0][c0] += 1
        bond[r1][c1] += 1

        return False

    if not backtracking():
        raise InvalidMoleculeException


if __name__ == '__main__':
    tc = 1
    while True:
        R, C = map(int, sys.stdin.readline().split())
        if (R, C) == (0, 0):
            break
        for r in range(R):
            for c, value in enumerate(sys.stdin.readline().strip()):
                GRID[r][c] = value
        try:
            validate(R, C, GRID)
        except InvalidMoleculeException:
            sys.stdout.write(f'Molecule {tc} is invalid.\n')
        else:
            sys.stdout.write(f'Molecule {tc} is valid.\n')
        tc += 1
