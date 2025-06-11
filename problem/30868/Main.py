import sys


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    result = ['++++'] * (n//5)
    result.append('|'*(n%5))
    sys.stdout.write(' '.join(result)+'\n')
