from typing import *
from collections import defaultdict
from dataclasses import dataclass, field
import sys


DY = (-1, -1, -1, 0, 1, 1, 1, 0, )
DX = (1, 0, -1, -1, -1, 0, 1, 1, )

H = 4
W = 4


@dataclass
class Field:
    grid: Dict[Tuple[int, int], Tuple[int, int]] = field(default_factory=lambda: defaultdict(lambda: [None, 0]))
    fish: Dict[int, Tuple[Optional[int], Optional[int]]] = field(default_factory=lambda: defaultdict(lambda: [None, None]))

    def print(self) -> str:
        lines = []
        for y in range(H):
            row = []
            for x in range(W):
                fish_id = self.get_fish_id(y, x)
                if fish_id is None:
                    row.append('[   ]')
                    continue
                d = self.get_fish_d(fish_id)
                f = f'{fish_id:02d}'+('↗↑↖←↙↓↘→'[d])
                if fish_id == 0:
                    row.append(f'<{f}>')
                else:
                    row.append(f'[{f}]')
            lines.append(''.join(row))
        return lines

    def get_fish_id(self, y: int, x: int) -> int:
        return self.grid[y, x][0]

    def get_fish_y(self, fish_id: int) -> int:
        return self.fish[fish_id][0]

    def get_fish_x(self, fish_id: int) -> int:
        return self.fish[fish_id][1]

    def get_fish_d(self, fish_id: int) -> int:
        y = self.get_fish_y(fish_id)
        x = self.get_fish_x(fish_id)
        return self.grid[y, x][1]

    def is_empty(self, y: int, x: int) -> bool:
        return self.grid[y, x][0] is None

    def is_shark(self, y: int, x: int) -> bool:
        return self.get_fish_id(y, x) == 0

    def is_fish(self, y: int, x: int) -> bool:
        return (not self.is_empty(y, x)) and (not self.is_shark(y, x))

    def is_bound(self, y: int, x: int) -> bool:
        return 0 <= y < H and 0 <= x < W

    def is_fish_dead(self, fish_id: int) -> bool:
        y = self.get_fish_y(fish_id)
        x = self.get_fish_x(fish_id)
        return y is None and x is None

    def set_fish_d(self, fish_id: int, d: int) -> int:
        y = self.get_fish_y(fish_id)
        x = self.get_fish_x(fish_id)
        self.grid[y, x][1] = d

    def set_shark(self, y: int, x: int) -> int:
        assert self.is_fish(y, x)
        shark_id = 0
        fish_id = self.get_fish_id(y, x)
        py = self.get_fish_y(shark_id)
        px = self.get_fish_x(shark_id)
        self.fish[fish_id][0] = None
        self.fish[fish_id][1] = None
        self.fish[shark_id][0] = y
        self.fish[shark_id][1] = x
        self.grid[py, px][0] = None
        self.grid[py, px][1] = None
        self.grid[y, x][0] = shark_id

    def move_fish(self, fish_id: int):
        y = self.get_fish_y(fish_id)
        x = self.get_fish_x(fish_id)
        d = self.get_fish_d(fish_id)
        for _ in range(8):
            ny = y+DY[d]
            nx = x+DX[d]
            if not self.is_bound(ny, nx):
                d = (d+1) % 8
                continue
            if self.is_shark(ny, nx):
                d = (d+1) % 8
                continue
            if self.is_empty(ny, nx):
                self.set_fish_d(fish_id, d)
                self.grid[y, x], self.grid[ny, nx] = self.grid[ny, nx], self.grid[y, x]
                self.fish[fish_id][0] = ny
                self.fish[fish_id][1] = nx
                break
            if self.is_fish(ny, nx):
                self.set_fish_d(fish_id, d)
                other_fish_id = self.get_fish_id(ny, nx)
                self.fish[fish_id], self.fish[other_fish_id] = self.fish[other_fish_id], self.fish[fish_id]
                self.grid[y, x], self.grid[ny, nx] = self.grid[ny, nx], self.grid[y, x]
                break

    def copy_from(self, other: 'Field'):
        for y, x in other.grid:
            self.grid[y, x][0] = other.grid[y, x][0]
            self.grid[y, x][1] = other.grid[y, x][1]
        for fish_id in other.fish:
            self.fish[fish_id][0] = other.fish[fish_id][0]
            self.fish[fish_id][1] = other.fish[fish_id][1]


FIELDS = defaultdict(Field)


def solve():
    moves = 0
    field = FIELDS[moves]
    for y in range(H):
        tokens = sys.stdin.readline().split()
        for x in range(W):
            fish_id = int(tokens[2*x])
            fish_direction = int(tokens[2*x+1]) % 8
            field.grid[y, x][0] = fish_id
            field.grid[y, x][1] = fish_direction
            field.fish[fish_id][0] = y
            field.fish[fish_id][1] = x
    victim_fish_id = field.get_fish_id(0, 0)
    field.set_shark(0, 0)
    return backtracking(moves) + victim_fish_id


def backtracking(moves: int) -> int:
    field = FIELDS[moves]
    for fish_id in range(1, 17):
        if not field.is_fish_dead(fish_id):
            field.move_fish(fish_id)
    max_eat_count = 0
    y = field.get_fish_y(0)
    x = field.get_fish_x(0)
    d = field.get_fish_d(0)
    while field.is_bound(y := y+DY[d], x := x+DX[d]):
        if field.is_fish(y, x):
            next_field = FIELDS[moves+1]
            next_field.copy_from(field)
            victim_fish_id = next_field.get_fish_id(y, x)
            next_field.set_shark(y, x)
            max_eat_count = max(max_eat_count, backtracking(moves+1)+victim_fish_id)
    return max_eat_count


answer = solve()
print(answer)
