# 9616번: 홀수 정사각형

# 좌상단 좌표를 (0, 0)이라고 할 때, x축 y축 위의 점 각각 하나 씩 정하면 그걸로 정사각형을 만들 수 있다.

import sys
import functools


def count_by_bbox(n: int) -> int:
    """바운딩 박스의 크기가 (square_size, square_size)인
    격자 위의 격자 정사각형의 개수.

    O(1)
    """
    return n


@functools.cache
def count_by_stretched_square(square_size: int) -> int:
    """정사각형 모양 격자의 크기가 (square_size, square_size)일 때,
    격자의 크기가 (square_size+1, square_size)로 변하면 늘어나는
    넓이가 홀수인 격자 위의 격자 정사각형의 개수.

    O(N)
    """
    answer = 0
    for bbox_size in range(1, square_size+1, 2):
        variant = (square_size - bbox_size + 1) # slide 해가면서 만들 수 있는 경우의 수
        answer += variant * count_by_bbox(bbox_size)
    return answer


@functools.cache
def count_by_square(square_size: int) -> int:
    """정사각형 모양 격자의 크기가 (square_size, square_size)일 때,
    넓이가 홀수인 격자 위의 격자 정사각형의 개수.

    O(N)
    """
    answer = 0
    for bbox_size in range(1, square_size+1, 2):
        variant = (square_size - bbox_size + 1) ** 2
        answer += variant * count_by_bbox(bbox_size)
    return answer


def solve(w: int, h: int) -> int:
    s_len = min(w, h) # shorter edge length
    l_len = max(w, h) # longer edge length

    answer = 0
    answer += count_by_square(s_len)
    answer += (l_len-s_len) * count_by_stretched_square(s_len)
    return answer


while (shape := tuple(map(int, sys.stdin.readline().split()))) != (0, 0):
    sys.stdout.write(f"{solve(*shape)}\n")
