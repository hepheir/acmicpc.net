# 10252번: 그리드 그래프

import collections
import sys


def is_even(x: int) -> bool:
    return x % 2 == 0


def solve():
    m, n = map(int, sys.stdin.readline().split())
    w, h = m, n
    print(1)
    if is_even(w) and is_even(h):
        for y in range(h):
            x_iterator = range(w) if is_even(y) else reversed(range(w))
            for x in x_iterator:
                print(f'({x},{y})')
    elif is_even(w):
        for x in range(w):
            y_iterator = range(h) if is_even(x) else reversed(range(h))
            for y in y_iterator:
                print(f'({x},{y})')
    elif is_even(h):
        for y in range(h):
            x_iterator = range(w) if is_even(y) else reversed(range(w))
            for x in x_iterator:
                print(f'({x},{y})')
    elif w < h:
        for y in range(h-w):
            x_iterator = range(w) if is_even(y) else reversed(range(w))
            for x in x_iterator:
                print(f'({x},{y})')
        x_iterator = collections.deque(range(w))
        for y in range(h-w, h):
            for x in x_iterator:
                print(f'({x},{y})')
            x_iterator.rotate(1)
    else:
        for x in range(w-h):
            y_iterator = range(h) if is_even(x) else reversed(range(h))
            for y in y_iterator:
                print(f'({x},{y})')
        y_iterator = collections.deque(range(h))
        for x in range(w-h, w):
            for y in y_iterator:
                print(f'({x},{y})')
            y_iterator.rotate(1)


T = int(sys.stdin.readline())
for _ in range(T):
    solve()
