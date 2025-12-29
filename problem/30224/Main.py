# 30224번: Lucky 7

n = input()

if '7' not in n:
    answer = 0 if int(n) % 7 else 1
else:
    answer = 2 if int(n) % 7 else 3

print(answer)
