# 13741번: Alphabet

import bisect

# Longest Increasing Sequence, O(N log N)
# https://namu.wiki/w/최장%20증가%20부분%20수열#s-3.2

A = list(map(ord, input().strip()))
N = len(A)
D = [0] * N
X = [ord('z')] * N

for i in range(N):
    j = bisect.bisect_left(X, A[i])
    D[i] = j + 1
    if X[j] > A[i]:
        X[j] = A[i]

answer = (ord('z')-ord('a')+1) - max(D)
print(answer)
