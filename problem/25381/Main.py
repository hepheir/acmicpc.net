import functools
import sys


MAX_S_LEN = 300000

sys.setrecursionlimit(10*MAX_S_LEN)


@functools.cache
def get_max_exec(S: str) -> int:
    max_exec = 0
    for i in range(len(S)):
        if not (S[i] == 'A' or S[i] == 'B'):
            continue
        for j in range(i+1, len(S)):
            if (S[i] == 'A' and S[j] == 'B') or (S[i] == 'B' and S[j] == 'C'):
                max_exec = max(max_exec, get_max_exec(S[:i]+S[i+1:j]+S[j+1:])+1)
    return max_exec


print(get_max_exec(S=sys.stdin.readline().strip()))
