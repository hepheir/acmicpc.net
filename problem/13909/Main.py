# 13909번: 창문 닫기


N = int(input())

answer = 0
bit_len = 1
step = 0
while bit_len <= N:
    answer += 1
    bit_len += 2*(step+1)+1
    step += 1

print(answer)
