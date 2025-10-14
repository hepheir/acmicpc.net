# 21043번: Domino Line

import sys

MAX_A = MAX_B = 50000


def solve(N, A: list[int], B: list[int]) -> int:
    adj = [[] for _ in range(MAX_A+1)]
    deg = [0] * (MAX_A+1)
    for i in range(N):
        adj[A[i]].append(B[i])
        adj[B[i]].append(A[i])
        deg[A[i]] += 1
        deg[B[i]] += 1

    visited = [False] * (MAX_A+1)

    def dfs(u: int) -> list:
        stack = []
        history = []
        visited[u] = True
        stack.append(u)
        history.append(u)
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if visited[v]:
                    continue
                visited[v] = True
                stack.append(v)
                history.append(v)
        return history

    answer = 0
    for u in range(1, MAX_A+1):
        if not adj[u] or visited[u]:
            continue
        odd = sum(deg[v] % 2 for v in dfs(u))
        answer += max(1, odd // 2)
    return answer


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
