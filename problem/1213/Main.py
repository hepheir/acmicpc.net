# 1213번: 팰린드롬 만들기

from collections import Counter

IMPOSSIBLE = "I'm Sorry Hansoo"
ALPHABETS = [chr(c) for c in range(ord('A'), ord('Z')+1)]

S = input().strip()
counts = Counter(S)

def solve(i: int):
    if i == len(ALPHABETS):
        if sum([cnt & 1 for cnt in counts.values()]) > 1:
            return False, IMPOSSIBLE
        for c, cnt in counts.items():
            if cnt & 1:
                return True, c
        return True, ''

    c = ALPHABETS[i]
    cnt = counts[c] >> 1

    is_possible, substring = solve(i+1)
    if is_possible:
        return True, c * cnt + substring + c * cnt
    return False, IMPOSSIBLE

print(solve(0)[1])
