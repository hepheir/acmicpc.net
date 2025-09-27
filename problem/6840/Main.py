# 6840번: Who is in the middle?

A = int(input())
B = int(input())
C = int(input())

if A > B:
    A, B = B, A
if A > C:
    A, C = C, A
if C < A:
    C, A = A, C
if C < B:
    C, B = B, C

print(B)
