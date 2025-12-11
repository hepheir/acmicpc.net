# 31846번: 문자열 접기

import sys

N = int(sys.stdin.readline())
S = ' '+sys.stdin.readline().strip()
Q = int(sys.stdin.readline())
for _ in range(Q):
    l, r = map(int, sys.stdin.readline().split())
    max_score = 0
    for s in range(l, r):
        e = s+1
        score = 0
        while l <= s and e <= r:
            if S[s] == S[e]:
                score += 1
            s -= 1
            e += 1
        max_score = max(max_score, score)
    print(max_score)
