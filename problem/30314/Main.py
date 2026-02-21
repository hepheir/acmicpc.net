# 30314번: Just a Joystick

n = int(input())
A = input().strip()
B = input().strip()

answer = 0
for i in range(n):
    answer += min(
        (ord(B[i]) - ord(A[i])) % 26,
        (ord(A[i]) - ord(B[i])) % 26,
    )

print(answer)
