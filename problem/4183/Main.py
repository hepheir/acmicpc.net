# 4183번: Unique Snowflakes

import sys
import collections


def max_unique_snowflakes(n: int, snowflakes: list) -> int:
    # sliding window or queue (as a two pointer)
    count = collections.Counter()
    max_window_size = 0
    j = 0
    for i in range(n):
        while j < i and count[snowflakes[i]] > 0:
            count[snowflakes[j]] -= 1
            j += 1
        count[snowflakes[i]] += 1
        max_window_size = max(max_window_size, i-j+1)
    return max_window_size


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        snowflakes = []
        for i in range(n):
            snowflakes.append(int(sys.stdin.readline()))
        answer = max_unique_snowflakes(n, snowflakes)
        sys.stdout.write(f'{answer}\n')
