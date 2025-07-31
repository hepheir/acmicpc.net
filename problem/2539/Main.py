# 2539번: 모자이크

import sys


H, W = map(int, sys.stdin.readline().split())
PAPER_COUNT = int(sys.stdin.readline())
TARGET_COUNT = int(sys.stdin.readline())
R = [0] * TARGET_COUNT
C = [0] * TARGET_COUNT

MAX_R = 0
MIN_C = W
MAX_C = 0

for i in range(TARGET_COUNT):
    R[i], C[i] = map(int, sys.stdin.readline().split())
    MAX_R = max(MAX_R, R[i])
    MIN_C = min(MIN_C, C[i])
    MAX_C = max(MAX_C, C[i])


C_ASC = sorted(C)

def estimate_paper_count(paper_size: int) -> int:
    coverage = 0
    paper_count = 0
    for c in C_ASC:
        if coverage < c:
            coverage = c+paper_size-1
            paper_count += 1
    return paper_count


lo = MAX_R
hi = H
while lo < hi:
    mid = (lo+hi)//2
    if estimate_paper_count(mid) > PAPER_COUNT:
        lo = mid+1
    else:
        hi = mid

print(lo)
