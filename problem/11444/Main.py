import sys


MOD = 1000000007


def mod_mult(a: int, b: int, m: int = MOD) -> int:
    return ((a % m) * (b % m)) % m


def mod_add(a: int, b: int, m: int = MOD) -> int:
    return ((a % m) + (b % m)) % m


def m_pow(exp: int) -> list[list[int]]:
    if exp == 1:
        return [[1,1],[1,0]]
    mat = m_pow(exp//2)
    mat = m_mult(mat, mat)
    if exp % 2 == 1:
        mat = m_mult(mat, m_pow(1))
    return mat


def m_mult(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    return [
        [
            mod_add(mod_mult(A[0][0], B[0][0]), mod_mult(A[0][1], B[1][0])),
            mod_add(mod_mult(A[0][0], B[0][1]), mod_mult(A[0][1], B[1][1])),
        ],
        [
            mod_add(mod_mult(A[1][0], B[0][0]), mod_mult(A[1][1], B[1][0])),
            mod_add(mod_mult(A[1][0], B[0][1]), mod_mult(A[1][1], B[1][1])),
        ],
    ]


def fib(n: int) -> int:
    if n == 0:
        return 0
    return m_pow(n-1)[0][0] % MOD


if __name__ == '__main__':
    sys.setrecursionlimit(int(1e7))

    n = int(sys.stdin.readline())
    print(fib(n))
