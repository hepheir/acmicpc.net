# 1058번: 친구

import sys

N = int(sys.stdin.readline())
dist = [ [sys.maxsize]*N for _ in range(N) ]

for i in range(N):
    for j, value in enumerate(sys.stdin.readline().strip()):
        if value == 'Y':
            dist[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

max_count = 0
for i in range(N):
    count = 0
    for j in range(N):
        if i != j and dist[i][j] <= 2:
            count += 1
    max_count = max(max_count, count)

print(max_count)
