# 6603번: 로또

import sys


def main():
    while True:
        k, *numbers = map(int, sys.stdin.readline().split())
        if k == 0:
            break
        print('\n'.join(solve(numbers, k, 6)))
        print()


def solve(arr: list[int], n: int, r: int):
    """arr[-n:] 에서 r개를 선택"""
    i = len(arr) - n
    if r <= 0 or n < r:
        return
    if r == 1:
        yield f'{arr[i]}'
    for substring in solve(arr, n-1, r-1):
        yield f'{arr[i]} {substring}'
    yield from solve(arr, n-1, r)


if __name__ == '__main__':
    main()
