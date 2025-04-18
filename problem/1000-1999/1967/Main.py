import heapq
import sys

graph: list[list[tuple[int, int]]]
visited: list[bool]


class MaxHeap:
    def __init__(self):
        self.items: list[int] = []

    def push(self, x: int):
        heapq.heappush(self.items, -x)

    def pop(self) -> int:
        return -heapq.heappop(self.items)

    def empty(self) -> bool:
        return len(self.items) == 0


MAX_N = 10000

sys.setrecursionlimit(2*MAX_N)

graph = [[] for n in range(MAX_N+1)]
visited = [False] * (MAX_N+1)
ans = 0



# 분할정복(DFS)으로 트리의 반지름 후보를 구하는 코드
def dfs(u: int) -> int:
    global ans
    visited[u] = True
    heap = MaxHeap()
    for v, w in graph[u]:
        if not visited[v]:
            heap.push(w+dfs(v))
    if not heap.empty():
        dist = heap.pop()
        if not heap.empty():
            # 이 노드가 지름의 중심일 경우
            ans = max(ans, dist+heap.pop())
        return dist
    return 0


# 입력 받기
n = int(sys.stdin.readline())
for i in range(n-1):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

# 트리의 지름 구하기
print(max(dfs(1), ans))
