import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    for _ in range(M):
        sys.stdin.readline()
    sys.stdout.write(f'{N-1}\n')
