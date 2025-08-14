# 1499번: 뒤집기 수열

MAX_N = 50
INF = MAX_N+1


def r(A: list, B: list) -> int:
    i = 0
    j = len(A)
    swap_count = 0
    while i < j-1:
        while i < j and A[i] == B[i]:
            i += 1
        while i < j and A[j-1] == B[j-1]:
            j -= 1
        if i < j-1:
            if A[i] == A[j-1]:
                return -1
            A[i:j] = A[i:j][::-1]
            swap_count += 1
    return swap_count if A[i:j] == B[i:j] else -1


if __name__ == '__main__':
    A = list(input().strip())
    B = list(input().strip())
    answer = r(A, B)
    print(answer)
