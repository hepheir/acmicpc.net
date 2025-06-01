N = int(input())
A = [*map(int, input().split())]

mapper = {}
for src, dst in zip(sorted(range(N), key=lambda i: A[i]), range(N)):
    mapper[src] = dst

P = [mapper[i] for i in range(N)]

print(*P)
