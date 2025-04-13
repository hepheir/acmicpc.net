import sys


N, M = map(int, sys.stdin.readline().split())
D = [0] + [int(sys.stdin.readline()) for _ in range(N)]

max_dist = [[0] * (M+1) for _ in range(N+2)]


for time in range(1, N+1):
    for tireacy in range(M+1):
        if time+tireacy <= N+1:
            max_dist[time+max(tireacy, 1)][0] = max(max_dist[time+max(tireacy, 1)][0], max_dist[time][tireacy])
        if tireacy+1 <= M:
            max_dist[time+1][tireacy+1] = max(max_dist[time+1][tireacy+1], max_dist[time][tireacy]+D[time])


print(max_dist[N+1][0])
