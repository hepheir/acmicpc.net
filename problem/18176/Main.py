# 18176번: Zeldain Garden

"""memo

문제의 정답은 [N,M] 구간의 정수들의 약수들을 모은 집합의 크기이다.
다만, N <= 10^12 로 매우 크다.
대강 O(sqrt(N) log N) 시간 이내에 문제의 정답을 구해야 하는 상황.
"""


def count_factors(n: int) -> int:
    # O(sqrt(n))
    retval = 0
    for i in range(1, int(n**0.5)+1):
        if n % i != 0:
            continue
        retval += 1
        if n // i == i:
            continue
        retval += 1
    return retval


def solve(N: int, M: int) -> int:
    return sum(count_factors(i) for i in range(N, M+1))


if __name__ == '__main__':
    N, M = map(int, input().split())
    answer = solve(N, M)
    print(answer)
