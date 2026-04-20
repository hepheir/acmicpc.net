# 32625번: 분할

import sys


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))


def is_possible(window_size: int) -> bool:
    if N % window_size != 0:
        return False
    prev_min_max_sum = None
    for offset in range(0, N, window_size):
        min_val = sys.maxsize
        max_val = 0
        for i in range(offset, offset+window_size):
            min_val = min(min_val, A[i])
            max_val = max(max_val, A[i])
        min_max_sum = min_val + max_val
        if prev_min_max_sum is not None and min_max_sum != prev_min_max_sum:
            return False
        prev_min_max_sum = min_max_sum
    return True


for window_size in range(1, (N//2)+1):
    if is_possible(window_size):
        print('1')
        break
else:
    print('0')
