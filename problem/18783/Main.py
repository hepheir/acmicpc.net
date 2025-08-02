# 18783번: Swapity Swapity Swap

import sys


N, M, K = map(int, sys.stdin.readline().split())

# O(NM)
MAPPER_DIFF = {i:i for i in range(1, N+1)}
for _ in range(M):
    L, R = map(int, sys.stdin.readline().split())
    window_size = R-L+1
    for offset in range(window_size//2):
        l = L+offset
        r = R-offset
        MAPPER_DIFF[l], MAPPER_DIFF[r] = MAPPER_DIFF[r], MAPPER_DIFF[l]


def is_initial_state(mapper: dict) -> bool:
    for i in range(1, N+1):
        if mapper[i] != i:
            return False
    return True


def simulate_once(mapper: dict) -> dict:
    return {i: MAPPER_DIFF[mapper[i]] for i in range(1, N+1)}


# Find out period.
mapper = {i: i for i in range(1, N+1)}
period = 1
while not is_initial_state((mapper := simulate_once(mapper))):
    period += 1


# The actual simulation
mapper = {i: i for i in range(1, N+1)}
for _ in range(K % period):
    mapper = simulate_once(mapper)


# Print the answer
for i in range(1, N+1):
    sys.stdout.write(f'{mapper[i]}\n')
