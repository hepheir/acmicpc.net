# 5341번: Pyramids

import sys


# 등차수열의 합 공식
for n in map(int, sys.stdin.read().split()):
    if n == 0:
        break
    sys.stdout.write(f'{n*(n+1)//2}\n')
