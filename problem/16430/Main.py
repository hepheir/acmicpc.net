from math import gcd

A, B = map(int, input().split())

P = (B-A)
Q = B

P, Q = P//gcd(P, Q), Q//gcd(P, Q)
print(P, Q)
