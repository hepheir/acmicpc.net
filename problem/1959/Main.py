# 1959번: 달팽이3


M, N = map(int, input().split())

padding_x = M // 2 if M % 2 else (M // 2)-1
padding_y = N // 2 if N % 2 else (N // 2)-1
padding = min(padding_x, padding_y)

rotation = 4 * padding

x_min = padding+1
x_max = N-padding
y_min = padding+1
y_max = M-padding

if y_min == y_max:
    x = x_max
    y = y_max
elif x_min == x_max:
    rotation += 1
    x = x_max
    y = y_max
elif y_min+1 == y_max:
    rotation += 2
    x = x_min
    y = y_min+1
elif x_min+1 == x_max:
    rotation += 3
    x = x_min
    y = y_min+1

print(rotation)
print(y, x)
