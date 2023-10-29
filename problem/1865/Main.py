import sys


def testcase(tc: int):
    N, M, W = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, -T))

    # Bellman-ford
    dist = [ None ] + [ sys.maxsize ]*N
    prev = [ None ] + [ None ]*N
    dist[1] = 0
    # edge relaxation repeatedly
    for i in range(N-1):
        for u, v, w in edges:
            if dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
                prev[v] = u
    # check for negative cycles
    for u, v, w in edges:
        if dist[v] > dist[u]+w:
            print('YES')
            return
    print('NO')


if __name__ == "__main__":
    for tc in range(int(sys.stdin.readline())):
        testcase(tc)