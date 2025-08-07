# 9625번: BABBA

K = int(input())

A_count = 1
B_count = 0

for _ in range(K):
    # 뭔가 피보나치 같네
    A_count, B_count = B_count, B_count+A_count

print(A_count, B_count)