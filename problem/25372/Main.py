# 25172번: 성택이의 은밀한 비밀번호

import sys


N = int(sys.stdin.readline())
for _ in range(N):
    S = sys.stdin.readline().strip()
    if 6 <= len(S) <= 9:
        sys.stdout.write('yes\n')
    else:
        sys.stdout.write('no\n')
