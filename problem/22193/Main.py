# 22193번: Multiply

N, M = map(int, input().split())
A = list(map(int, input().strip()[::-1]))
B = list(map(int, input().strip()[::-1]))
C = [0] * (N + M)
for i in range(N):
    for j in range(M):
        C[i + j] += A[i] * B[j]
        for k in range(i + j, N + M):
            if C[k] < 10:
                break
            C[k + 1] += C[k] // 10
            C[k] %= 10
answer = ''.join(map(str, C[::-1])).lstrip('0')
answer = answer if answer else '0'

print(answer)
