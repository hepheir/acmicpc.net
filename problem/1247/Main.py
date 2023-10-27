import sys

for t in range(3):
    N = int(sys.stdin.readline())
    ans = sum(int(sys.stdin.readline()) for n in range(N))
    if ans == 0:
        print('0')
    elif ans < 0:
        print('-')
    else:
        print('+')
