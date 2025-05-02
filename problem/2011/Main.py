from functools import cache


MOD = 1000000

code = tuple(map(int, input().strip()))


@cache
def count_cases(i: int = 0) -> int:
    """i번째 글자부터 나올 수 있는 경우의 수."""
    if i == len(code):
        return 1
    cases = 0
    if 1 <= code[i] <= 9:
        cases += count_cases(i+1)
    if (i+1) < len(code) and 10 <= (10*code[i]+code[i+1]) <= 26:
        cases += count_cases(i+2)
    return cases % MOD


# pre-cache, so recursion won't get in deep when calling `count_cases(0)`
for i in reversed(range(len(code))):
    count_cases(i)

print(count_cases())
