# 11290번: Wonowon


def get_primes(hi: int):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(hi**0.5)+1):
        if sieve[i]:
            for j in range(i*i, hi+1, i):
                sieve[j] = False
    for i in range(2, hi+1):
        if sieve[i]:
            yield i


def W(p: int, hi: int) -> int:
    number = 1
    length = 1
    while length <= hi:
        if number % p == 0:
            return length
        number = number * 100 + 1
        length += 2
    return -1


if __name__ == '__main__':
    n = int(input())
    answer = 0
    for p in get_primes(n):
        if W(p, p-2) == p-2:
            answer += 1

    print(answer)
