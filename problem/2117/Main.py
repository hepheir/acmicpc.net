# 2117번: 원형 댄스


def solve(n: int) -> int:
    if n % 2 == 0:
        return (n // 2) * ((n-1) // 2)
    else:
        return (n // 2) * (n // 2)


n = int(input())
print(solve(n))
