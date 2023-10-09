# N은 최대 18자리 숫자.
# 그리디 + 백트래킹으로 풀어보자.

def solve(N: list[int], K: int):
    def _solve(N: list[int], K: int, stack: list[int]):
        if K < 0:
            return
        if not N:
            if K == 0:
                # Found answer!
                print(''.join(map(str, stack)))
                exit()
            return
        for n in range(N[0], 10):
            k = K
            if n not in stack:
                k -= 1
            _solve(N[1:], k, stack+[n])
            N = [0] * len(N)

    for n in range(N[0], 10):
        _solve(N[1:], K-1, [n])
        N = [0] * len(N)


if __name__ == "__main__":
    N_raw, K_raw = input().split()

    N = list(map(int, N_raw))
    K = int(K_raw)

    solve(N, K)
