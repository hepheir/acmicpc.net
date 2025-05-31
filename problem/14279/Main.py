a, b, c = map(int, input().split())


def calculate_value(A: int, B: int) -> int:
    return abs(A-a) + abs(B-b) + abs(A*B-c)


min_value = min(calculate_value(a, b), calculate_value(0, 0))
max_diff = min_value

A_diff = 0
while A_diff < max_diff:
    B_diff = 0
    while B_diff < (max_diff-A_diff):
        for A, B in [(a-A_diff, b-B_diff), (a-A_diff, b+B_diff), (a+A_diff, b-B_diff), (a+A_diff, b+B_diff)]:
            if A <= 0 or B <= 0:
                continue
            value = calculate_value(A, B)
            if min_value > value:
                min_value = value
                max_diff = min(max_diff, A_diff+B_diff)
        B_diff += 1
    A_diff += 1


print(min_value)
