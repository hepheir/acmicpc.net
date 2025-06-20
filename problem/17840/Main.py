import sys


Q, M = map(int, sys.stdin.readline().split())

# Pisano period 라는 것이 있었다. (ㅡㅡ ;;)
# : 피보나치 수열의 mod M 은 주기를 가지며, 주기는 반드시 0, 1로 시작한다는 내용.
# https://www.geeksforgeeks.org/fibonacci-number-modulo-m-and-pisano-period/

PISANO_SEQUENCE = [0, 1, ]

f_curr = 1
f_prev = 1
while True:
    PISANO_SEQUENCE.append(f_curr)
    if PISANO_SEQUENCE[-2] == 0 and PISANO_SEQUENCE[-1] == 1:
        PISANO_SEQUENCE.pop()
        PISANO_SEQUENCE.pop()
        break
    f_curr, f_prev = (f_curr+f_prev) % M, f_curr

PERIOD = len(PISANO_SEQUENCE)
SEQUENCE = ''.join(map(str, PISANO_SEQUENCE))


for _ in range(Q):
    N = int(sys.stdin.readline())
    N %= len(SEQUENCE)
    sys.stdout.write(f"{SEQUENCE[N]}\n")
