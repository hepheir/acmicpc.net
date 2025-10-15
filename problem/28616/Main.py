# 28616번: Биомаркеры

import sys

MAX_K = int(5e5)


def main():
    K = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    print(solve(K, S))


def solve(K: int, S: str) -> str:
    digits = {0: [], 1: [], 2: []}
    count = {0: 0, 1: 0, 2: 0}
    for i in range(K):
        digit = int(S[i])
        digits[digit % 3].append((digit, i))
        count[digit % 3] += 1
    for r in range(3):
        digits[r].sort()

    def bigint_key(s: str):
        return len(s), s

    def solve_util(rm_0: int, rm_1: int, rm_2: int) -> str:
        string = list(S)
        for i in range(rm_0):
            string[digits[0][i][1]] = ''
        for i in range(rm_1):
            string[digits[1][i][1]] = ''
        for i in range(rm_2):
            string[digits[2][i][1]] = ''
        return ''.join(string)

    ans = []
    rem = (count[1] + 2*count[2]) % 3
    if rem == 0:
        if count[0] >= 1:
            # 0을 1개 제거.
            ans.append(solve_util(1, 0, 0))
        if count[1] >= 3:
            # 1를 3개 제거.
            ans.append(solve_util(0, 3, 0))
        if count[2] >= 3:
            # 2를 3개 제거.
            pass
        if count[1] >= 1 and count[2] >= 1:
            # 1를 1개, 2를 1개 제거.
            ans.append(solve_util(0, 1, 1))
    if rem == 1:
        if count[1] >= 1:
            # 1을 1개 제거.
            ans.append(solve_util(0, 1, 0))
        if count[2] >= 2:
            # 2를 2개 제거.
            ans.append(solve_util(0, 0, 2))
    if rem == 2:
        if count[1] >= 2:
            # 1을 2개 제거.
            ans.append(solve_util(0, 2, 0))
        if count[2] >= 1:
            # 2를 1개 제거.
            ans.append(solve_util(0, 0, 1))

    return max(ans, key=bigint_key)


if __name__ == '__main__':
    main()
