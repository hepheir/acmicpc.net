# 31887번: 앳코더 스터디

import sys

INF = sys.maxsize


N, M = map(int, sys.stdin.readline().split())
a = [*map(int, sys.stdin.readline().split()), 0] # zero-padding for -1 index.

is_target = [False] * (2*N)
for i in range(M):
    is_target[a[i]] = True


time_pos = [INF] * (2*N+1)
time_pos[N] = 0
for offset in range(1, N):
    time_pos[offset], time_pos[offset+N] = (
        min(
            time_pos[offset-1] + (2 if is_target[offset+N] else 1),
            time_pos[offset+N-1] + 2,
        ),
        min(
            time_pos[offset+N-1] + (2 if is_target[offset] else 1),
            time_pos[offset-1] + 2
        )
    )

time_neg = [INF] * (2*N+1)
time_neg[N] = 0
for offset in reversed(range(1, N)):
    time_neg[offset], time_neg[offset+N] = (
        min(
            time_neg[offset+1] + (2 if is_target[offset+N] else 1),
            time_neg[offset+N+1] + 2,
        ),
        min(
            time_neg[offset+N+1] + (2 if is_target[offset] else 1),
            time_neg[offset+1] + 2
        )
    )


min_time = INF
for i in range(-1, M):
    time = 0
    if a[i] > 0:
        # 위에서 추가한 zero-padding을 이용한다.
        time += time_pos[a[i]]
    for x in range(a[i]+1, N+N):
        if is_target[x]:
            time += time_neg[x]
            break
        if x < N and is_target[x+N]:
            time += time_neg[x+N]
            break
        if x > N and is_target[x-N]:
            time += time_neg[x-N]
            break
    if min_time > time:
        min_time = time


print(min_time)
