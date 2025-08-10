# 9616번: 홀수 정사각형

import sys
import functools


def count_by_bbox(square_size: int) -> int:
    """바운딩 박스의 크기가 (square_size, square_size)인
    격자 위의 격자 정사각형의 개수.

    O(1)
    """
    return square_size


@functools.cache
def count_by_stretched_square(square_size: int) -> int:
    """정사각형 모양 격자의 크기가 (square_size, square_size)일 때,
    격자의 크기가 (square_size+1, square_size)로 변하면 늘어나는
    넓이가 홀수인 격자 위의 격자 정사각형의 개수.

    아래의 식을 단순화함.

    ```
    answer = 0
    for bbox_size in range(1, square_size+1, 2):
        variant = (square_size - bbox_size + 1) # slide 해가면서 만들 수 있는 경우의 수
        answer += variant * count_by_bbox(bbox_size)
    ```

    \\sum_{x=0}{n} (y-(2x+1))(2x+1) = -\\frac{(n+1)(4n^2+n(8-3y)-3y+3)}{3}

    O(1)
    """
    n = square_size // 2
    y = square_size+1
    return -((n+1)*(4*n*n+n*(8-3*y)-3*y+3))//3


@functools.cache
def count_by_square(square_size: int) -> int:
    """정사각형 모양 격자의 크기가 (square_size, square_size)일 때,
    넓이가 홀수인 격자 위의 격자 정사각형의 개수.

    아래의 식을 단순화함.

    ```
    answer = 0
    for bbox_size in range(1, square_size+1, 2):
        variant = (square_size - bbox_size + 1) ** 2
        answer += variant * count_by_bbox(bbox_size)
    ```

    \\sum_{x=0}{n} (y-(2x+1))^2 (2x+1) = \\frac{(n+1)(6n^3+n^2(18-8y)+n(3y^2-16y+15)+3(y-1)^2)}{3}

    O(1)
    """
    n = square_size // 2
    y = square_size+1
    return ((n+1)*(6*n*n*n + n*n*(18-8*y)+n*(3*y*y-16*y+15)+3*(y-1)**2))//3


def solve(w: int, h: int) -> int:
    s_len = min(w, h)  # shorter edge length
    l_len = max(w, h)  # longer edge length

    answer = 0
    answer += count_by_square(s_len)
    answer += (l_len-s_len) * count_by_stretched_square(s_len)
    return answer


while (shape := tuple(map(int, sys.stdin.readline().split()))) != (0, 0):
    sys.stdout.write(f"{solve(*shape)}\n")
