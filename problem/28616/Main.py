# 28616번: Биомаркеры

import sys


sys.setrecursionlimit(int(1e7))


def main():
    K = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    print(solve(K, S))


def solve(K: int, S: str) -> int:
    arr = list(map(int, S))

    # zero-padded for -1 indexing
    dp_dropped_o = [[0, 0, 0] for _ in range(K+1)]
    dp_dropped_x = [[0, 0, 0] for _ in range(K+1)]

    for i in range(K):
        for r in range(3):
            dp_dropped_o[i][r] = max(dp_dropped_o[i-1][r], dp_dropped_o[i][r])

            value = 10*dp_dropped_x[i-1][r] + arr[i]
            dp_dropped_o[i][r] = max(dp_dropped_x[i][r], dp_dropped_o[i][r])
            dp_dropped_o[i][value % 3] = max(value, dp_dropped_o[i][value % 3])
            dp_dropped_x[i][value % 3] = max(value, dp_dropped_x[i][value % 3])

            value = 10*dp_dropped_o[i-1][r] + arr[i]
            dp_dropped_o[i][value % 3] = max(value, dp_dropped_o[i][value % 3])

    return dp_dropped_o[K-1][0]


if __name__ == '__main__':
    main()
