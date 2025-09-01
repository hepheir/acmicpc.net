# 2538번: 모눈종이 자르기

from typing import List, Tuple
import sys


def solve(W: int, H: int, vertex: List[Tuple[int, int]]) -> int:
    for x, y in vertex:
        # 다각형의 변이 테두리에 닿는지 확인하기.
        if x == 0 or x == W or y == 0 or y == H:
            break
    else:
        perimeter = 2*(W+H) + calc_perimeter(vertex)
        return 1, perimeter

    perimeters = []
    vertex_segment = get_vertex_segment(W, H, vertex)
    for i in range(len(vertex_segment)):
        if len(vertex_segment[i]) < 2:
            continue
        polygon = close_polygon(W, H, vertex_segment[i])
        perimeter = calc_perimeter(polygon)
        if perimeter > 0:
            perimeters.append(perimeter)

    return len(perimeters), max(perimeters)


def get_vertex_segment(W: int, H: int, vertex: List[Tuple[int, int]]) -> List[List[Tuple[int, int]]]:
    vertex_segment: List[List[Tuple[int, int]]] = [[]]
    for s in range(len(vertex)):
        x, y = vertex[s]
        if x == 0 or x == W or y == 0 or y == H:
            break
    for i in range(s, s+len(vertex)+1):
        i %= len(vertex)
        x, y = vertex[i]
        if x == 0 or x == W or y == 0 or y == H:
            vertex_segment[-1].append(vertex[i])
            vertex_segment.append([])
        vertex_segment[-1].append(vertex[i])
    return vertex_segment


def calc_perimeter(polygon: List[Tuple[int, int]]) -> int:
    perimeter = 0
    for i in range(len(polygon)):
        cx, cy = polygon[i]
        px, py = polygon[i-1]
        dx, dy = cx-px, cy-py
        perimeter += abs(dx)+abs(dy)
    return perimeter


def close_polygon(W: int, H: int, vertex: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    # 다각형이 아니면 빈 정점 리스트를 반환.
    if len(vertex) <= 1:
        return []
    if len(vertex) == 2:
        cx, cy = vertex[0]
        nx, ny = vertex[1]
        dx, dy = nx-cx, ny-cy
        if dx == 0 and (cx == 0 or cx == W):
            return []
        if dy == 0 and (cy == 0 or cy == H):
            return []
    vertex = vertex.copy()
    px, py = vertex[-2]
    cx, cy = vertex[-1]
    dx, dy = cx-px, cy-py
    if dx:
        vertex.append((W, 0) if dx > 0 else (0, H))
    if dy:
        vertex.append((W, H) if dy > 0 else (0, 0))
    cx, cy = vertex[0]
    nx, ny = vertex[1]
    dx, dy = nx-cx, ny-cy
    if dx:
        vertex.append((0, 0) if dx > 0 else (W, H))
    if dy:
        vertex.append((W, 0) if dy > 0 else (0, H))
    return vertex


def main():
    W, H = map(int, sys.stdin.readline().split())
    V = int(sys.stdin.readline())
    vertex = []
    for _ in range(V):
        x, y = map(int, sys.stdin.readline().split())
        vertex.append((x, y))
    n_segments, perimeter = solve(W, H, vertex)
    print(n_segments, perimeter)


if __name__ == '__main__':
    main()
