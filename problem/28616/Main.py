# 28616번: Биомаркеры

import sys

MAX_K = int(5e5)


def main():
    K = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    print(solve(K, S))


def solve(K: int, S: str) -> str:
    digits = {
        0: [],
        1: [],
        2: [],
    }
    for i, n in enumerate(map(int, S)):
        digits[n % 3].append((n, i))

    def bigint_key(s: str):
        return len(s), s

    def remove_char(S: str, rem: int) -> str:
        j = -1
        for i in range(len(S)):
            n = int(S[i])
            if n % 3 != rem:
                continue
            j = i
            if i+1 < len(S) and int(S[i]) <= int(S[i+1]):
                break
        assert j != -1
        return S[:j] + S[j+1:]


    ans = []
    rem = (len(digits[1]) + 2*len(digits[2])) % 3
    if rem == 0:
        if len(digits[0]) >= 1:
            # 0을 1개 제거.
            ans.append(remove_char(S, 0))
        if len(digits[1]) >= 1 and len(digits[2]) >= 1:
            # 1를 1개, 2를 1개 제거.
            ans.append(remove_char(remove_char(S, 1), 2))
        if len(digits[1]) >= 3:
            # 1를 3개 제거.
            ans.append(remove_char(remove_char(remove_char(S, 1), 1), 1))
        if len(digits[2]) >= 3:
            # 2를 3개 제거.
            ans.append(remove_char(remove_char(remove_char(S, 2), 2), 2))
    if rem == 1:
        if len(digits[1]) >= 1:
            # 1을 1개 제거.
            ans.append(remove_char(S, 1))
        if len(digits[2]) >= 2:
            # 2를 2개 제거.
            ans.append(remove_char(remove_char(S, 2), 2))
    if rem == 2:
        if len(digits[2]) >= 1:
            # 2를 1개 제거.
            ans.append(remove_char(S, 2))
        if len(digits[1]) >= 2:
            # 1을 2개 제거.
            ans.append(remove_char(remove_char(S, 1), 1))
    return max(ans, default='0', key=bigint_key)


if __name__ == '__main__':
    main()
