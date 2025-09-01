# 2538번: 모눈종이 자르기

from typing import List, Tuple
import sys


def solve(W: int, H: int, vertex: List[Tuple[int, int]]) -> int:
    for x, y in vertex:
        if x == 0 or x == W or y == 0 or y == H:
            break
    else:
        # 색종이가 나뉘지 않는 경우.
        perimeter = 2*(W+H) + calc_polygon_perimeter(vertex)
        return 1, perimeter

    perimeters = [*map(calc_polygon_perimeter, get_polygons(W, H, vertex))]
    if not perimeters:
        return 0, 0
    return len(perimeters), max(perimeters)


def get_polygons(W: int, H: int, vertex: List[Tuple[int, int]]) -> List[List[Tuple[int, int]]]:
    corner = [(0, 0), (W, 0), (W, H), (0, H)]

    def is_end_of_edge(i: int) -> bool:
        cx, cy = vertex[i]
        px, py = vertex[i-1]
        dx, dy = cx-px, cy-py
        return (dx == 0 and cx*(cx-W) == 0) or (dy == 0 and cy*(cy-H) == 0)

    def partition_vertices(start: int) -> List[List[Tuple[int, int]]]:
        partition: List[List[Tuple[int, int]]] = [[]]
        for i in range(start, start+len(vertex)):
            i %= len(vertex)
            if not is_end_of_edge(i):
                partition[-1].append(vertex[i])
            elif len(partition[-1]) <= 1:
                partition[-1].clear()
                partition[-1].append(vertex[i])
            else:
                partition.append([vertex[i]])
        return partition

    def close_polygon(vertex: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        "색종이의 꼭짓점을 포함하여 다각형의 모든 정점을 표시한다."
        vertex = vertex.copy()
        # 첫 번째 코너 찾기
        dx, dy = (vertex[-1][0]-vertex[-2][0]), (vertex[-1][1]-vertex[-2][1])
        if dx > 0: i = 1
        if dx < 0: i = 3
        if dy > 0: i = 2
        if dy < 0: i = 0
        # 3개 이상의 변을 색종이와 공유하는 경우 예외처리
        if abs(vertex[0][0]-vertex[-1][0]) * abs(vertex[0][1]-vertex[-1][1]) == 0:
            vertex.append(corner[i])
            i -= 1
        while True:
            vertex.append(corner[i])
            if (corner[i][0] == vertex[0][0]) or (corner[i][1] == vertex[0][1]):
                break
            i -= 1
        return vertex

    for i in range(len(vertex)):
        if is_end_of_edge(i):
            return [*map(close_polygon, partition_vertices(i))]
    else:
        return [vertex]


def calc_polygon_perimeter(polygon: List[Tuple[int, int]]) -> int:
    perimeter = 0
    for i in range(len(polygon)):
        cx, cy = polygon[i]
        px, py = polygon[i-1]
        dx, dy = cx-px, cy-py
        perimeter += abs(dx)+abs(dy)
    return perimeter


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
