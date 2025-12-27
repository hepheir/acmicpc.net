# 27328번: 三方比較 (Three-Way Comparison)

A = int(input())
B = int(input())
if A == B:
    print(0)
else:
    diff = A-B
    print(diff//abs(diff))
