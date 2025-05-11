import collections
import sys


graph_win = collections.defaultdict(set)
graph_lose = collections.defaultdict(set)

queue = collections.deque()

team_rank = collections.defaultdict(int)
teams_per_rank = collections.defaultdict(list)


# Initialize directed graphs (!!! we assumes DAG !!!)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph_win[i].add(j)
    graph_lose[j].add(i)


# Find winner candidates (teams that never lost)

for node in range(1, n+1):
    if not graph_lose[node]:
        team_rank[node] = 1
        queue.append(node)


# Estimate ranking status for other nodes via graph traversal

while queue:
    node = queue.popleft()
    for next_node in tuple(graph_win[node]):
        graph_lose[next_node].remove(node)
        if graph_lose[next_node]:
            # 이 노드를 이긴 노드를 먼저 보는것이 옳으므로 지금은 방문하지 않는다.
            continue
        team_rank[next_node] = team_rank[node] + 1
        graph_win[node].remove(next_node)
        queue.append(next_node)


# Look into the rank distribution

for node in range(1, n+1):
    teams_per_rank[team_rank[node]].append(node)


# Print teams line by line, ordered by their ranks

is_determinded = True
for rank in range(1, max(teams_per_rank)+1):
    is_determinded &= (len(teams_per_rank[rank]) == 1)
    for node in teams_per_rank[rank]:
        sys.stdout.write(f'{node}\n')

sys.stdout.write(f'{0 if is_determinded else 1}\n')
