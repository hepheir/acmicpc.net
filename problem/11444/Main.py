MOD = 1000000007
FIBO_MAT = [[1,1],[1,0]]


def mod_mult(a: int, b: int, m: int = MOD) -> int:
    return ((a % m) * (b % m)) % m


def mod_add(a: int, b: int, m: int = MOD) -> int:
    return ((a % m) + (b % m)) % m


def m_copy(mat: list[list[int]]) -> list[list[int]]:
    return [[mat[0][0], mat[0][1]], [mat[1][0], mat[1][1]]]


def m_pow(mat: list[list[int]], exp: int):
    if exp == 1:
        return
    m_pow(mat, exp//2)
    m_mult(mat, mat)
    if exp % 2 == 1:
        m_mult(mat, FIBO_MAT)


def m_mult(mat: list[list[int]], other: list[list[int]]):
    a = mod_add(mod_mult(mat[0][0], other[0][0]), mod_mult(mat[0][1], other[1][0]))
    b = mod_add(mod_mult(mat[0][0], other[0][1]), mod_mult(mat[0][1], other[1][1]))
    c = mod_add(mod_mult(mat[1][0], other[0][0]), mod_mult(mat[1][1], other[1][0]))
    d = mod_add(mod_mult(mat[1][0], other[0][1]), mod_mult(mat[1][1], other[1][1]))
    mat[0][0] = a
    mat[0][1] = b
    mat[1][0] = c
    mat[1][1] = d


def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    fibo_mat = m_copy(FIBO_MAT)
    m_pow(fibo_mat, n-1)
    return fibo_mat[0][0]


if __name__ == '__main__':
    n = int(input())
    print(fib(n))
