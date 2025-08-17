# 24371번: БРОЙ ПОДНИЗОВЕ

import math

S = input().strip()  # S의 모든 문자는 서로 다르다.
P = input().strip()

s_set = set(S)
p_set = set(P)

answer = 0

# P의 모든 문자는 서로 달라야한다.
total_char_count = len(s_set - p_set)
if len(P) == len(p_set) and total_char_count == len(s_set) - len(p_set):
    for char_count in range(total_char_count+1):
        answer += math.comb(total_char_count, char_count) * math.perm(char_count) * (char_count+1)

print(answer)
