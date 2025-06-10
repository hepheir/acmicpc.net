import dataclasses
import sys


MAX_R = 5
MAX_C = 5

DR = (-1, 0, 0, 1,)
DC = (0, -1, 1, 0,)

BOND_COUNT = {
    '.': 0,
    'H': 1,
    'O': 2,
    'N': 3,
    'C': 4,
}

grid = [[None] * MAX_C for _ in range(MAX_R)]
R = 0
C = 0


@dataclasses.dataclass
class Context:
    R: int = 0
    C: int = 0
    grid: list = dataclasses.field(default_factory=lambda: [[0] * MAX_C for _ in range(MAX_R)])

    def is_bound(self, r: int, c: int) -> bool:
        return 0 <= r < self.R and 0 <= c < self.C

    def get_edges(self):
        edges = []
        for sr in range(self.R):
            for sc in range(self.C):
                for er, ec in ((sr, sc+1), (sr+1, sc)):
                    if not self.is_bound(er, ec):
                        continue
                    if self.grid[er][ec] == 0:
                        continue
                    edges.append((sr, sc, er, ec))
        return edges

    def get_total_bonds(self) -> int:
        bonds = 0
        for r in range(self.R):
            for c in range(self.C):
                bonds += self.grid[r][c]
        return bonds

    def is_valid(self) -> bool:
        edges = self.get_edges()
        max_bonds = self.get_total_bonds()

        if max_bonds % 2 == 1:
            return False

        def backtracking(i: int = 0, bonds: int = 0) -> bool:
            if i == len(edges):
                return bonds == max_bonds
            if bonds > max_bonds:
                return False
            sr, sc, er, ec = edges[i]
            if self.grid[sr][sc] > 0 and self.grid[er][ec] > 0:
                self.grid[sr][sc] -= 1
                self.grid[er][ec] -= 1
                is_valid = backtracking(i+1, bonds+2)
                self.grid[sr][sc] += 1
                self.grid[er][ec] += 1
                if is_valid:
                    return True
            return backtracking(i+1, bonds)

        sys.setrecursionlimit(10*len(edges)+1000)
        return backtracking()


ctx = Context()
tc = 1
while True:
    ctx.R, ctx.C = map(int, sys.stdin.readline().split())
    if (ctx.R, ctx.C) == (0, 0):
        break
    for r in range(ctx.R):
        for c, value in enumerate(sys.stdin.readline().strip()):
            ctx.grid[r][c] = BOND_COUNT[value]
    sys.stdout.write(f'Molecule {tc} is {"valid" if ctx.is_valid() else "invalid"}.\n')
    tc += 1
