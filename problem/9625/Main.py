# 9625번: BABBA

K = int(input())

curr = ['A']
prev = []
for _ in range(K):
    curr, prev = prev, curr
    curr.clear()
    for c in prev:
        if c == 'A':
            curr.append('B')
        else:
            curr.append('B')
            curr.append('A')

A_count = 0
B_count = 0

for c in curr:
    if c == 'A':
        A_count += 1
    else:
        B_count += 1

print(A_count, B_count)
