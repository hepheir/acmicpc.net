# 28616번: Биомаркеры

import sys

MAX_K = int(5e5)


def main():
    K = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    answer = solve(K, S)
    print(answer)


def max_str(*args: str) -> str:
    s = [s for s in args if not s.startswith('*')]
    s.sort(key=len, reverse=True)
    if not s:
        return '*'
    while s and len(s[0]) != len(s[-1]):
        s.pop()
    return max(s)


def solve(K: int, S: str) -> str:
    dp_prev = ['*', '*', '*']
    dp_curr = ['*', '*', '*']
    for i in range(K):
        dp_prev, dp_curr = dp_curr, dp_prev
        n = int(S[i])
        for r in range(3):
            dp_curr[r] = dp_prev[r]
        dp_curr[n % 3] = max_str(S[i], dp_curr[n % 3])
        for r in range(3):
            dp_curr[(r+n) % 3] = max_str(dp_prev[r]+S[i], dp_curr[(r+n) % 3])
        pass
    answer = dp_curr[0]
    if answer == '*':
        return '0'
    return str(int(answer))


if __name__ == '__main__':
    main()
