# 2623번: 음악프로그램

import collections
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

indegree = [0] * (N+1)

for _ in range(M):
    singer_count, *singers = map(int, sys.stdin.readline().split())
    for i in range(1, singer_count):
        graph[singers[i]].append(singers[i-1])
        indegree[singers[i-1]] += 1

queue = collections.deque(range(1, N+1)) # 아직 정렬되지 않은 노드
stack = [] # 정렬 결과
node = -1

# 위상 정렬
for i in range(1, N+1):
    for _ in range(N):
        node = queue.popleft()
        if indegree[node] == 0:
            stack.append(node)
            for next_node in graph[node]:
                indegree[next_node] -= 1
            break
        queue.append(node)
    else:
        # 순서 정하기 불가능
        print(0)
        break

print(*reversed(stack), sep='\n')
