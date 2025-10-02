# 11403번: 경로 찾기

import sys

V = int(sys.stdin.readline())
dist = [[*map(int, sys.stdin.readline().split())] for _ in range(V)]

for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][k] + dist[k][j] == 2:
                dist[i][j] = 1

for u in range(V):
    for v in range(V):
        print(dist[u][v], end=' ')
    print()
