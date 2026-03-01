# 1322번: X와 K


def main():
    X, K = map(int, input().split())
    answer = solve(X, K+1, X.bit_length())
    print(answer)


def solve(X: int, K: int, bit_len: int) -> int:
    if K == 1:
        return 0
    if (count := get_count(X, bit_len)) < K:
        return solve(X, K, bit_len+1)
    if (count := get_count(X, bit_len-1)) < K:
        Y = 1 << (bit_len-1)
        return solve(X, K - count, bit_len-1) | Y
    return solve(X, K, bit_len-1)


def get_count(X: int, bit_len: int) -> int:
    count = 1
    for i in range(bit_len):
        if X & (1 << i) == 0:
            count <<= 1  # power of 2
    return count


if __name__ == '__main__':
    main()
