# 32374번: 선물 고르기

import collections
import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))

G = collections.Counter()

for i in range(N):
    G[B[i]] += 1

# 앞 사람이 선물을 가져감
for i in range(K):
    G[C[i]] -= 1

# 남아있는 선물 상자 중 가장 큰 것의 크기
my_box_size = max(box_size for box_size in G if G[box_size] > 0)

biggest_gift_size = 0
for i in range(N):
    if A[i] > my_box_size:
        continue
    biggest_gift_size = max(biggest_gift_size, A[i])

print(biggest_gift_size)
