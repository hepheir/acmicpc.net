from typing import Tuple

Matrix_2x2 = Tuple[int, int, int, int]

MOD = int(1e6)
F = (1, 1, 1, 0)
I = (1, 0, 0, 1)


def matrix_dot(A: Matrix_2x2, B: Matrix_2x2) -> Matrix_2x2:
    return (
        (A[0]*B[0]+A[1]*B[2]) % MOD,
        (A[0]*B[1]+A[1]*B[3]) % MOD,
        (A[2]*B[0]+A[3]*B[2]) % MOD,
        (A[2]*B[1]+A[3]*B[3]) % MOD,
    )


def matrix_pow(A: Matrix_2x2, exp: int) -> Matrix_2x2:
    # Exponentiation by squaring, O(log N), (N=exp)
    if exp == 0:
        return I
    ans = matrix_pow(A, exp//2)
    ans = matrix_dot(ans, ans)
    if exp % 2:
        ans = matrix_dot(ans, A)
    return ans


if __name__ == '__main__':
    n = int(input())
    ans = matrix_pow(F, n+1)[3]
    print(ans)
