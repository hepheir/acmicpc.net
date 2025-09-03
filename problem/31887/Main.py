# 31887번: 앳코더 스터디

import functools
import sys


MAX_N = int(1e6)
INF = sys.maxsize

sys.setrecursionlimit(100*MAX_N)


N, M = map(int, sys.stdin.readline().split())

a = [*map(int, sys.stdin.readline().split()), 0] # zero-padding for -1 index.

is_target = [False] * (2*N)
for i in range(M):
    is_target[a[i]] = True


@functools.cache
def calc_time(n: int, step: int) -> int:
    """1번 동작에서 무조건 step=(-1 or +1) 만큼 움직일 때,
    1, 2, 3번 동작을 이용하여 n번 건물까지 이동하면서
    방문 가능한 건물에 있는 모든 근수를 데리고 돌아오는데 걸린 시간.
    """
    if not (1 <= n <= (2*N-1)):
        return INF
    if n < N:
        return 1 + min(
            calc_time(n+N-step, step) + 1,
            calc_time(n-step, step) + (1 if is_target[n+N] else 0),
        )
    if n > N:
        return 1 + min(
            calc_time(n-N-step, step) + 1,
            calc_time(n-step, step) + (1 if is_target[n-N] else 0),
        )
    return 0


min_time = INF
for i in range(-1, M):
    time = 0
    if a[i] > 0:
        # 위에서 추가한 zero-padding을 이용한다.
        time += calc_time(a[i], +1)
    for x in range(a[i]+1, 2*N):
        if is_target[x]:
            time += calc_time(x, -1)
            break
        if x < N and is_target[x+N]:
            time += calc_time(x+N, -1)
            break
        if x > N and is_target[x-N]:
            time += calc_time(x-N, -1)
            break
    if min_time > time:
        min_time = time

print(min_time)
