import collections
import functools
import sys


@functools.cache
def calc_dist(mbti_1: str, mbti_2: str) -> int:
    d = 0
    for i in range(4):
        if mbti_1[i] != mbti_2[i]:
            d += 1
    return d


def testcase(testcase_no: int):
    sys.stdin.readline()
    # O(N)
    counter = collections.Counter(sys.stdin.readline().split())

    most_common = counter.most_common()
    n = len(most_common) # n은 최대 16. (=MBTI 경우의 수)

    min_dist = sys.maxsize
    # O(1), T(n) = 16^3
    for i in range(n):
        if most_common[i][1] >= 3:
        # 3
            min_dist = 0
            continue
        if most_common[i][1] == 2:
        # 2 + 1
            for j in range(i+1, n):
                dist = 2 * calc_dist(most_common[i][0], most_common[j][0])
                min_dist = min(min_dist, dist)
            continue
        # 1 + 1 + 1
        for j in range(i+1, n):
            for k in range(j+1, n):
                dist = calc_dist(most_common[i][0], most_common[j][0])
                dist += calc_dist(most_common[i][0], most_common[k][0])
                dist += calc_dist(most_common[j][0], most_common[k][0])
                min_dist = min(min_dist, dist)
    print(min_dist)


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for tc in range(T):
        testcase(tc)
