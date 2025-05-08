import functools
import sys


N = int(input())
*NUMBERS, ANSWER = map(int, sys.stdin.readline().split())


@functools.cache
def solve(i: int = 0, x: int = 0) -> int:
    """NUMBERS[:i] 들을 조합해서 x를 만들었을때, 등식을 만족시키는 경우의 수."""
    if i == len(NUMBERS):
        return 1 if (x == ANSWER) else 0
    cases = 0
    for y in (x-NUMBERS[i], x+NUMBERS[i]):
        if 0 <= y <= 20:
            cases += solve(i+1, y)
    return cases


print(solve())
