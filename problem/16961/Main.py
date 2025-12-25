# 16961번: 탭 vs 공백

import sys

MAX_DAYS = 366

N = int(sys.stdin.readline())


people = []
for _ in range(N):
    c, s, e = sys.stdin.readline().split()
    s = int(s)
    e = int(e)
    people.append((c, s, e))


def solve_1():
    # 1. 투숙객이 1명 이상인 날의 수
    count = [0] * (MAX_DAYS+1)
    for c, s, e in people:
        for day in range(s, e+1):
            count[day] += 1
    answer = 0
    for day in range(MAX_DAYS+1):
        if count[day] > 0:
            answer += 1
    return answer


def solve_2():
    # 2. 가장 많은 투숙객이 있었던 날에 투숙한 사람의 수
    count = [0] * (MAX_DAYS+1)
    for c, s, e in people:
        for day in range(s, e+1):
            count[day] += 1
    return max(count)


def solve_3():
    # 3. 싸움이 없는 날의 수
    counts = {
        'T': [0] * (MAX_DAYS+1),
        'S': [0] * (MAX_DAYS+1),
    }
    for c, s, e in people:
        for day in range(s, e+1):
            counts[c][day] += 1
    answer = 0
    for day in range(MAX_DAYS+1):
        if counts['S'][day] == counts['T'][day] > 0:
            answer += 1
    return answer


def solve_4():
    # 4. 싸움이 없는 날 중 가장 많은 투숙객이 있었던 날에 투숙한 사람의 수. 싸움이 없는 날이 없으면 0을 출력한다.
    counts = {
        'T': [0] * (MAX_DAYS+1),
        'S': [0] * (MAX_DAYS+1),
    }
    for c, s, e in people:
        for day in range(s, e+1):
            counts[c][day] += 1
    answer = 0
    for day in range(MAX_DAYS+1):
        if counts['S'][day] == counts['T'][day] > 0:
            answer = max(counts['S'][day]+counts['T'][day], answer)
    return answer


def solve_5():
    # 5. 가장 오랜 기간 투숙한 사람이 투숙한 날의 수
    answer = 0
    for c, s, e in people:
        answer = max(e-s+1, answer)
    return answer


print(solve_1())
print(solve_2())
print(solve_3())
print(solve_4())
print(solve_5())
