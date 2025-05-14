import sys


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
SENSOR = sorted(set(map(int, sys.stdin.readline().split())))

edges = []
for i in range(len(SENSOR)-1):
    edges.append(SENSOR[i+1] - SENSOR[i])
edges.sort()

while K > 1 and edges:
    edges.pop()
    K -= 1

print(sum(edges))
