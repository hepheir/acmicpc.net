# 17370번: 육각형 우리 속의 개미


def solve(N: int) -> int:
    answer = 0
    visited = set()

    def dfs(px: int = None, py: int = None, x: int = 0, y: int = 0, d: int = 0):
        nonlocal answer
        if (x, y) in visited:
            answer += 1 if (d == N+1) else 0
            return
        if d > N:
            return
        visited.add((x, y))
        children = [
            (x-1, y),
            (x, y-1 if (x+y) % 2 == 0 else y+1),
            (x+1, y),
        ]
        for nx, ny in children:
            if (px, py) == (nx, ny):
                continue
            dfs(x, y, nx, ny, d+1)
        visited.discard((x, y))

    # 첫 방향은 북쪽으로 고정
    visited.add((0, 0))
    dfs(0, 0, 0, -1, 1)
    return answer


if __name__ == '__main__':
    N = int(input())
    answer = solve(N)
    print(answer)
