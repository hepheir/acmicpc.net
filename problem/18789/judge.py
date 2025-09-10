from pathlib import Path
from heapq import heappush, heappop
from typing import List


def judge(grid: List[List[int]], W: int, H: int) -> int:
    heap = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] > 0:
                heappush(heap, (grid[i][j], i, j))
    score = 0
    while heap:
        top = heappop(heap)
        while heap[0] == top:
            heappop(heap)
        x, i, j = top
        if x > score+1:
            break
        score = max(score, x)
        for di in (-1, 0, +1):
            for dj in (-1, 0, +1):
                if di == 0 and dj == 0:
                    continue
                if not (0 <= i+di < H and 0 <= j+dj < W):
                    continue
                ni = i+di
                nj = j+dj
                nx = x*10+grid[ni][nj]
                heappush(heap, (nx, ni, nj))
    return score


if __name__ == '__main__':
    W = 14
    H = 8
    grid = [[None] * W for _ in range(H)]
    file = Path(__file__).parent / 'Main.txt'
    assert file.exists()
    with file.open('rt') as f:
        for i in range(H):
            line = f.readline().strip()
            for j in range(W):
                grid[i][j] = int(line[j])
    score = judge(grid, W, H)
    print('Score:', score)
