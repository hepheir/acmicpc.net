# 6975번: Deficient, Perfect, and Abundant

import sys


def proper_divisors(n: int):
    # O(sqrt(n))
    for i in range(1, int(n**0.5)+1):
        if n % i != 0:
            continue
        yield i
        if n == i*i or i == 1:
            continue
        yield n // i


args = list(map(int, sys.stdin.read().split()))
for i in range(1, len(args)):
    n = args[i]
    sum_of_divisors = sum(proper_divisors(n))
    if sum_of_divisors < n:
        sys.stdout.write(f'{n} is a deficient number.\n\n')
    elif sum_of_divisors == n:
        sys.stdout.write(f'{n} is a perfect number.\n\n')
    else:
        sys.stdout.write(f'{n} is an abundant number.\n\n')
