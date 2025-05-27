a, b, c = map(int, input().split())


def calculate_value(A: int, B: int) -> int:
    return abs(A-a) + abs(B-b) + abs(A*B-c)


def solve_with_fixed_A(A: int) -> int:
    hi = int(1e13)
    lo = 1
    while lo < hi:
        mid = (hi+lo)//2
        if calculate_value(A, mid) < calculate_value(A, mid+1):
            hi = mid
        else:
            lo = mid+1
    return calculate_value(A, lo)


def solve_with_bruteforcing_A() -> int:
    min_value = int(1e13)
    for A in range(1, 2*a+1):
        if min_value > (value := solve_with_fixed_A(A)):
            min_value = value
    return min_value


print(solve_with_bruteforcing_A())
