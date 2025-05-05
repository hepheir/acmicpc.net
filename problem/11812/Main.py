import sys

"""
K = 1 (-1 /1), max_depth = 1e15
1
2
3

K = 2, (+0 /2), max_depth = 49
   1
 2   3
4 5 6 7

K = 3, (+1 /3), max_depth = 32
         1
  2      3         4
5 6 7  8 9 10  11 12 13

K = 5, (+3 /5), max_depth = 22
                                    1
    2              3                4              5         6
7 8 9 10 11  12 13 14 15 16  17 18 19 20 21  22 23 24 25 26
"""


def get_dist(x: int, y: int, K: int) -> int:
    if K == 1:
        return abs(x-y)
    dist = 0
    while x != y:
        if x > y:
            x = get_parent(x, K)
        else:
            y = get_parent(y, K)
        dist += 1
    return dist


def get_parent(u: int, K: int) -> int:
    return (u+K-2) // K


N, K, Q = map(int, sys.stdin.readline().split())
for _ in range(Q):
    x, y = map(int, sys.stdin.readline().split())
    sys.stdout.write(f'{get_dist(x, y, K)}\n')
