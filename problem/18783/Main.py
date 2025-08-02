# 18783번: Swapity Swapity Swap

import sys


N, M, K = map(int, sys.stdin.readline().split())

# 입력을 토대로 Permutation 을 구성한다. O(NM)
PERMUTATION = list(range(N)) # Zero-base
for _ in range(M):
    L, R = map(int, sys.stdin.readline().split())
    window_size = R-L+1
    for offset in range(window_size//2):
        l = L+offset-1
        r = R-offset-1
        PERMUTATION[l], PERMUTATION[r] = PERMUTATION[r], PERMUTATION[l]


# 모든 사이클을 찾는다. O(N)
cycles = []
visited = [False] * N
for i in range(N):
    if visited[i]:
        continue
    cycle = [i]
    visited[i] = True
    while PERMUTATION[cycle[-1]] != i:
        cycle.append(PERMUTATION[cycle[-1]])
        visited[cycle[-1]] = True
    cycles.append(cycle)


# 각 사이클 별로 소들을 움직인다. O(N)
# (사이클들의 모든 원소의 개수의 합은 N이다.)
answer = [0] * N
for cycle in cycles:
    offset = K % len(cycle)
    for i in range(len(cycle)):
        answer[cycle[i]] = cycle[(i+offset) % len(cycle)]


# 정답을 출력한다.
for i in range(N):
    sys.stdout.write(f'{answer[i]+1}\n')
