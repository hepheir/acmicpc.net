from collections import Counter


def solve() -> bool:
    N = int(input())
    counter = Counter(map(int, input().split()))

    min_node = min(counter)
    max_node = max(counter)

    # 올라가지도 내려가지도 못하는 경우.
    if min_node == max_node:
        return False

    edges = 2 * counter[min_node]

    for node in range(min_node+1, max_node):
        if 2*counter[node] <= edges:
            return False

        edges = 2 * counter[node] - edges

        if (edges <= 0) or (edges % 2):
            return False

    return edges == (2 * counter[max_node])


if solve():
    print(1)
else:
    print(-1)
