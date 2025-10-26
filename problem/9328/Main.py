# 9328번: 열쇠

import sys
from collections import defaultdict
from typing import List


def solve(h: int, w: int, board: List[str], keys: str) -> int:
    doors_at = defaultdict(list)
    has_key = defaultdict(bool)
    for door_name in keys.lower():
        has_key[door_name] = True
    visited = defaultdict(lambda: defaultdict(bool))
    stack = []
    for y in range(h):
        for x in (0, w-1):
            if not visited[y][x]:
                visited[y][x] = True
                stack.append((y, x))
    for y in (0, h-1):
        for x in range(w):
            if not visited[y][x]:
                visited[y][x] = True
                stack.append((y, x))
    documents = 0
    while stack:
        y, x = stack.pop()
        cell: str = board[y][x]
        if cell == '*':
            continue
        elif cell == '$':
            documents += 1
        elif cell == '.':
            pass
        elif cell.islower():
            door_name = cell.lower()
            has_key[door_name] = True
            while doors_at[door_name]:
                ny, nx = doors_at[door_name].pop()
                visited[ny][nx] = True
                stack.append((ny, nx))
        elif cell.isupper():
            door_name = cell.lower()
            if not has_key[door_name]:
                doors_at[door_name].append((y, x))
                continue
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx]:
                visited[ny][nx] = True
                stack.append((ny, nx))
    return documents


T = int(sys.stdin.readline())
for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    board = [sys.stdin.readline().strip() for _ in range(h)]
    keys = sys.stdin.readline().strip()
    answer = solve(h, w, board, keys)
    print(answer)
