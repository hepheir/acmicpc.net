import sys


def l2_norm(x: float, y: float) -> float:
    return (x*x+y*y)**0.5


INF = 100000
MAX_N = 1000

X = [0] * MAX_N
Y = [0] * MAX_N
DIST = [[0] * MAX_N for _ in range(MAX_N)]

N = int(sys.stdin.readline())

for i in range(N):
    X[i], Y[i] = map(int, sys.stdin.readline().split())
    for j in range(i):
        d = l2_norm(X[i]-X[j], Y[i]-Y[j])
        DIST[i][j] = d
        DIST[j][i] = d

i = min(range(N), key=lambda i: max(DIST[i][:N]))
print(X[i], Y[i])
