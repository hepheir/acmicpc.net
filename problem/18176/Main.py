# 18176번: Zeldain Garden

"""memo

문제의 정답은 [N,M] 구간의 정수들의 약수들을 모은 집합의 크기이다.
다만, N <= 10^12 로 매우 크다.
대강 O(sqrt(N) log N) 시간 이내에 문제의 정답을 구해야 하는 상황.
"""


def solve(N: int, M: int) -> int:
    def solve_util(N: int) -> int:
        """[1..N] 구간의 정수 각각의 약수 개수의 합을 구하는 함수.
        O(sqrt(N))

        핵심 컨셉:
        i = [1..N] 에서, (i의 배수의 개수)의 합을 구한다.
        """
        answer = 0
        i = 1
        while i <= N:
            n_divisors = N // i

            # j = (n_divisors 보다 적은 '배수의 개수'를 갖는 다음 i)
            j = (N // n_divisors) + 1

            answer += n_divisors * (j-i)
            i = j
        return answer

    return solve_util(M) - solve_util(N-1)


if __name__ == '__main__':
    N, M = map(int, input().split())
    answer = solve(N, M)
    print(answer)
