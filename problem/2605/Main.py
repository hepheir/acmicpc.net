# 2605번: 줄 세우기

N = int(input())
stack = []
for student, i in enumerate(map(int, input().split()), start=1):
    stack.insert(len(stack)-i, student)

print(*stack)
