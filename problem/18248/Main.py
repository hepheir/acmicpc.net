# 18248번: 제야의 종

import functools
import sys


N, M = map(int, sys.stdin.readline().split())

a = [[False] * M for _ in range(N)]

for i in range(N):
    for j, v in enumerate(map(int, sys.stdin.readline().split())):
        a[i][j] = (v == 1)


@functools.cache
def heard_count(i: int) -> int:
    count = 0
    for j in range(M):
        count += a[i][j]
    return count


should_hear = [True] * M

try:
    # 많이 들은 사람 순으로 검증하자.
    for i in sorted(range(N), key=heard_count, reverse=True):
        for j in range(M):
            if a[i][j] == should_hear[j]:
                continue

            # 내 앞 사람은 들었는데, 나는 못 들은 경우
            if a[i][j] == False and should_hear[j] == True:
                should_hear[j] = False
                continue

            # 환청? 이 경우는 있으면 안됨.
            raise ValueError()

except ValueError:
    print('NO')
else:
    print('YES')
