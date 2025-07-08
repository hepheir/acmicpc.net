# 33692번: 해밍 거리


def solve(A: int, B: int):
    bit_len = max(A.bit_length(), B.bit_length())
    bin_a = list(f'{A:0{bit_len}b}')
    bin_b = list(f'{B:0{bit_len}b}')
    for i in range(bit_len):
        if bin_a[i] == bin_b[i]:
            continue
        bin_a[i] = '1'
        bin_b[i] = '0'
        for j in range(i+1, bit_len):
            bin_a[j] = '0'
            bin_b[j] = '1'
        break
    dec_a = int(''.join(bin_a), base=2)
    dec_b = int(''.join(bin_b), base=2)
    return dec_a, dec_b


if __name__ == '__main__':
    A, B = map(int, input().split())
    ans_A, ans_B = solve(A, B)
    print(ans_A, ans_B)
