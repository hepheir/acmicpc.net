# 2566번: 최댓값

max_value = -1
max_r = -1
max_c = -1
for r in range(1, 10):
    for c, value in enumerate(map(int, input().split()), start=1):
        if max_value < value:
            max_value = value
            max_r = r
            max_c = c

print(max_value)
print(max_r, max_c)
