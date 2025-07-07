# 14626번: ISBN


ISBN = input().strip()

missing_multiplier = None
check_sum = int(ISBN[-1])

for i in range(len(ISBN)-1):
    if i % 2 == 0:
        multiplier = 1
    else:
        multiplier = 3

    if ISBN[i] == '*':
        missing_multiplier = multiplier
    else:
        check_sum += int(ISBN[i]) * multiplier

answer = (10 - check_sum) % 10
while answer % missing_multiplier:
    answer += 10
answer //= missing_multiplier

print(answer)
