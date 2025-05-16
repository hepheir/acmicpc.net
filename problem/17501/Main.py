import sys


N = int(sys.stdin.readline())
sys.setrecursionlimit(10*(2*N))

root = 2*N-1
lchild = [None] * (2*N+1)
rchild = [None] * (2*N+1)
operator = [None] * (2*N+1)
numbers = [int(sys.stdin.readline()) for _ in range(1, N+1)]

positive_nodes = 0
negative_nodes = 0

for node in range(N+1, 2*N):
    op, u, v = sys.stdin.readline().split()
    lchild[node] = int(u)
    rchild[node] = int(v)
    operator[node] = op

def dfs(node: int, sign: int = 1):
    global positive_nodes, negative_nodes
    if (lchild[node] is None) and (rchild[node] is None):
        if sign > 0:
            positive_nodes += 1
        else:
            negative_nodes += 1
        return
    if lchild[node]:
        lsign = sign
        dfs(lchild[node], lsign)
    if rchild[node]:
        rsign = sign
        if operator[node] == '-':
            rsign = -rsign
        dfs(rchild[node], rsign)

dfs(root)


numbers.sort()
answer = sum(numbers[negative_nodes:]) - sum(numbers[:negative_nodes])
print(answer)
