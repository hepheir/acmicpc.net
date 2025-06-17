import sys


N, K = map(int, sys.stdin.readline().split())
STARTING_NUMBER, *NUMBERS = map(int, sys.stdin.readline().split())

dp_prev = [False] * K
dp_curr = [False] * K

dp_curr[STARTING_NUMBER % K] = True

for number in NUMBERS:
    dp_prev, dp_curr = dp_curr, dp_prev
    for k in range(K):
        dp_curr[k] = False
    for k in range(K):
        if dp_prev[k]:
            dp_curr[(k-number) % K] = True
            dp_curr[(k+number) % K] = True

if dp_curr[0]:
    sys.stdout.write("Divisible\n")
else:
    sys.stdout.write("Not divisible\n")
