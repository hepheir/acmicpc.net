from typing import List, Tuple, Iterable
from collections import defaultdict
import sys


def generate(password: List[int], diff: int, i: int = 0) -> Iterable[Tuple[int]]:
    if i == len(password):
        yield tuple()
    else:
        for others in generate(password, diff, i+1):
            if password[i]+diff <= 9:
                yield tuple([password[i]+diff, *others])
            if password[i]-diff >= 0:
                yield tuple([password[i]-diff, *others])


T = int(sys.stdin.readline())
for n in range(1, T+1):
    N = int(sys.stdin.readline())
    G = defaultdict(list)
    for i in range(N):
        u = tuple(map(int, sys.stdin.readline().strip()))
        G[u].clear()
        for diff in range(10):
            for v in generate(u, diff):
                if u != v and v in G:
                    G[v].append(u)
                    G[u].append(v)

    visited = defaultdict(bool)
    answer = 0
    for u in G:
        if not visited[u]:
            visited[u] = True
            for v in G[u]:
                visited[v] = True
            answer += 1

    sys.stdout.write(f"Case {n}: {answer}\n")
