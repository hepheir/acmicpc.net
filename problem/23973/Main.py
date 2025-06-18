import sys


def main():
    H, W = map(int, sys.stdin.readline().split())
    grid = [[0] * W for _ in range(H)]
    for y in range(H):
        for x, is_hit in enumerate(map(int, sys.stdin.readline().strip())):
            grid[y][x] = is_hit
    for cy in range(H):
        for cx in range(W):
            if is_valid(grid, H, W, cy, cx):
                sys.stdout.write(f'{cy} {cx}\n')
                return
    sys.stdout.write('-1\n')


def is_valid(grid: list, H: int, W: int, cy: int, cx: int) -> bool:
    for score in range(10, 0, -1):
        if not is_valid_score(grid, H, W, cy, cx, score):
            return False
    return True


def is_valid_score(grid: list, H: int, W: int, cy: int, cx: int, score: int) -> int:
    if score == 10:
        return 1 if grid[cy][cx] else 0
    radius = 10-score
    min_x = cx-radius
    max_x = cx+radius
    min_y = cy-radius
    max_y = cy+radius
    count = 0
    for x in range(max(min_x, 0), min(max_x, W-1)+1):
        if 0 <= (y := min_y) < H:
            count += grid[y][x]
        if 0 <= (y := max_y) < H:
            count += grid[y][x]
        if count > 1:
            return False
    for y in range(max(min_y+1, 0), min(max_y-1, H-1)+1):
        if 0 <= (x := min_x) < W:
            count += grid[y][x]
        if 0 <= (x := max_x) < W:
            count += grid[y][x]
        if count > 1:
            return False
    return count == 1


main()
