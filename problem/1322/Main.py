# 1322번: X와 K


def solve(X: int, K: int) -> int:
    Y = 0
    y_i = 0
    for k_i in range(K.bit_length()):
        while X & (1 << y_i) != 0:
            y_i += 1
        if K & (1 << k_i) != 0:
            Y |= 1 << y_i
        y_i += 1
    return Y


X, K = map(int, input().split())
print(solve(X, K))
