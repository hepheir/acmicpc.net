# 2538번: 모눈종이 자르기

from typing import List, Tuple
import sys


def dist(u: Tuple[int, int], v: Tuple[int, int]) -> int:
    ux, uy = u
    vx, vy = v
    dx, dy = vx-ux, vy-uy
    return abs(dx+dy)


def solve(W: int, H: int, vertex: List[Tuple[int, int]]) -> int:
    PERIMETER = 2*(W+H)

    def is_edge_on_outer(u: Tuple[int, int], v: Tuple[int, int]) -> bool:
        """두 정점을 잇는 간선이 색종이의 테두리 위에 있는지 여부."""
        ux, uy = u
        vx, vy = v
        dx, dy = vx-ux, vy-uy
        return (dx == 0 and (ux == 0 or ux == W)) or (dy == 0 and (uy == 0 or uy == H))

    def cvt_vertex_to_outer_position(u: Tuple[int, int]) -> int:
        """색종이 테두리를 1자로 폈을 때를 기준으로 한 좌표.
        (0, 0) 부터 반시계 방향으로 진행.
        """
        x, y = u
        if y == 0: return x
        if x == W: return W + y
        if y == H: return W + H + (W-x)
        if x == 0: return W + H + W + (H-y)


    if not any(is_edge_on_outer(vertex[i-1], vertex[i]) for i in range(len(vertex))):
        perimeter = sum(dist(vertex[i-1], vertex[i]) for i in range(len(vertex)))
        perimeter += PERIMETER
        return 1, perimeter

    perimeters = []

    offset = 0
    while offset < len(vertex):
        s = (offset-1) % len(vertex)
        inner_perimeter = 0
        while True:
            i = offset % len(vertex)
            if is_edge_on_outer(vertex[i-1], vertex[i]):
                break
            inner_perimeter += dist(vertex[i-1], vertex[i])
            offset += 1
        e = (offset-1) % len(vertex)
        try:
            outer_perimeter = (
                +cvt_vertex_to_outer_position(vertex[e])
                -cvt_vertex_to_outer_position(vertex[s])
            ) % PERIMETER
            if inner_perimeter > 0:
                perimeters.append(inner_perimeter+outer_perimeter)
        except:
            pass
        while True:
            i = offset % len(vertex)
            if not is_edge_on_outer(vertex[i-1], vertex[i]):
                break
            offset += 1

    return len(perimeters), max(perimeters, default=0)


def main():
    # 문제의 2번째 줄이 지문의 입력 형식을 지키지 않고 있어서
    # 임시로 이렇게 받았다.
    # (일부 테스트케이스에서 W, H, V가 한 줄에 들어온다.)
    W, H, V, *args = map(int, sys.stdin.read().split())
    vertex = []
    for i in range(V):
        x, y = args[2*i], args[2*i+1]
        vertex.append((x, y))
    n_segments, perimeter = solve(W, H, vertex)
    print(n_segments, perimeter)


if __name__ == '__main__':
    main()
