import sys

INF = sys.maxsize

def solve(N: int, M: list[int], ADJ_MAT: list[list[int]]):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    continue
                ADJ_MAT[i][j] = min(ADJ_MAT[i][j], ADJ_MAT[i][k] + ADJ_MAT[k][j])
    for i in range(1, N+1):
        for j in range(1, N+1):
            if ADJ_MAT[i][j] == INF:
                ADJ_MAT[i][j] = 0
    for i in range(1, N+1):
        sys.stdout.write(' '.join(map(str, ADJ_MAT[i][1:]))+'\n')

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    mat = [[INF] * (N+1) for _ in range((N+1))]
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        mat[a][b] = min(mat[a][b], c)
    solve(N, M, mat)
