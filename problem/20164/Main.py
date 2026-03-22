# 20164번: 홀수 홀릭 호석


MAX_N = int(1e9)-1

min_odds = MAX_N
max_odds = 0


def count_odds(S: str) -> int:
    count = 0
    for d in map(int, S):
        if d % 2 == 1:
            count += 1
    return count


def solve(N: int, odds: int = 0):
    S = str(N)
    odds += count_odds(S)
    if len(S) == 1:
        global min_odds, max_odds
        min_odds = min(min_odds, odds)
        max_odds = max(max_odds, odds)
        return
    if len(S) == 2:
        nN = int(S[0]) + int(S[1])
        solve(nN, odds)
        return
    for i in range(1, len(S)-1):
        for j in range(i+1, len(S)):
            nN = int(S[:i]) + int(S[i:j]) + int(S[j:])
            solve(nN, odds)


solve(int(input()))
print(min_odds, max_odds)
