# 32281번: 유리구슬 (Glass Bead)

input()
answer = 0
for chunk in input().split('0'):
    n = len(chunk)
    answer += n * (n + 1) // 2
print(answer)
