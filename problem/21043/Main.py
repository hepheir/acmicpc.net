# 21043번: Domino Line

import sys

MAX_A = MAX_B = 50000


def solve(N, A: list[int], B: list[int]) -> int:
    G = [[] for _ in range(MAX_A+1)]
    for i in range(N):
        G[A[i]].append((i, B[i]))
        G[B[i]].append((i, A[i]))
    rank = [-1] * N
    stack = []
    for i in range(N):
        if rank[i] == -1:
            rank[i] = i
            stack.append(A[i])
            stack.append(B[i])
            while stack:
                u = stack.pop()
                for j, v in G[u]:
                    if rank[j] == -1:
                        rank[j] = i
                        stack.append(v)
                        break
    return len(set(rank) - set([-1]))


def main():
    N = int(sys.stdin.readline())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, sys.stdin.readline().split())
    answer = solve(N, A, B)
    print(answer)


if __name__ == '__main__':
    main()
