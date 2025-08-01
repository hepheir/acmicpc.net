# 24597번: Reversibly Cyclic Strings

import sys


s = sys.stdin.readline().strip()

if s[::-1] in (s+s):
    answer = 1
else:
    answer = 0

print(answer)
