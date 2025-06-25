# 30023번: 전구 상태 바꾸기

from typing import List
import sys

CVT_COLOR2INT = {
    'R': 0,
    'G': 1,
    'B': 2,
}

N = int(sys.stdin.readline())
S = [CVT_COLOR2INT[c] for c in sys.stdin.readline().strip()]


def solve(S: List[int], target: int) -> int:
    # 모든 색상 코드를 target로 만들기 위해 바꿔야 하는 전구의 상태 수.
    S = S.copy()
    count = 0
    for i in range(N-2):
        diff = (target+3-S[i]) % 3
        count += diff
        for j in range(i, i+3):
            S[j] = (S[j]+diff) % 3
    for i in range(N-2, N):
        if S[i] != target:
            return -1
    return count


answer = -1
for color in range(3):
    if (ans := solve(S, color)) != -1:
        if answer == -1:
            answer = ans
        else:
            answer = min(answer, ans)

sys.stdout.write(f"{answer}\n")
