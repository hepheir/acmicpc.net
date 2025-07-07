# 14626번: ISBN


ISBN = input().strip()
check_sum = 0

for i in range(len(ISBN)):
    if ISBN[i] == '*':
        continue
    if i % 2 == 0:
        check_sum += int(ISBN[i]) * 1
    else:
        check_sum += int(ISBN[i]) * 3

answer = (10 - check_sum) % 10
print(answer)
