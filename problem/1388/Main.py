import sys

HBAR = '-'
VBAR = '|'

N, M = map(int, sys.stdin.readline().split())

prev_line = None
n_tiles = 0

for y in range(N):
    line = sys.stdin.readline().strip()
    for x in range(M):
        if line[x] == HBAR:
            if x > 0 and line[x-1] == HBAR:
                continue
        else:
            if y > 0 and prev_line[x] == VBAR:
                continue
        n_tiles += 1
    prev_line = line

sys.stdout.write(str(n_tiles))