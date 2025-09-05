# 32173번: 새치기

N = int(input())
s = [0, *map(int, input().split())]

prefix_sum = [0] * (N+1)
for i in range(1, N+1):
    prefix_sum[i] = s[i] + prefix_sum[i-1]


def max_satisfaction(i: int) -> int:
    """맨 앞 사람의 번호가 i일 때, 최대 만족도."""
    return s[i] - prefix_sum[i-1]


answer = max(max_satisfaction(i) for i in range(1, N+1))
print(answer)
