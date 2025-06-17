from typing import List, Tuple, Iterable
from collections import defaultdict
import sys


def trie_insert(trie: dict, password: Tuple[int]):
    if not password:
        trie['leaf'] = True
        return
    num, *others = password
    if num not in trie:
        trie[num] = {}
    trie_insert(trie[num], others)


def trie_search(trie: dict, password: Tuple[int], diff: int) -> Iterable[Tuple[int]]:
    if not password:
        if trie.get('leaf', False):
            yield tuple()
        return
    num, *others = password
    for num_alt in (num-diff, num+diff):
        if not (0 <= num_alt <= 9 and num_alt in trie):
            continue
        for tail in trie_search(trie[num_alt], others, diff):
            yield (num_alt, *tail)


T = int(sys.stdin.readline())
for n in range(1, T+1):
    N = int(sys.stdin.readline())
    G = defaultdict(set)
    trie = {}
    for i in range(N):
        u = tuple(map(int, sys.stdin.readline().strip()))
        for diff in range(10):
            for v in trie_search(trie, u, diff):
                if u != v:
                    G[v].add(u)
                    G[u].add(v)
        trie_insert(trie, u)


    visited = defaultdict(bool)
    answer = 0
    for u in G:
        if not visited[u]:
            visited[u] = True
            for v in G[u]:
                visited[v] = True
            answer += 1

    sys.stdout.write(f"Case {n}: {answer}\n")
