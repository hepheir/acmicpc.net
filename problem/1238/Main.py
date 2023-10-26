from __future__ import annotations

import dataclasses
import sys
import typing


T = typing.TypeVar('T')


@dataclasses.dataclass
class Vertex:
    i: int
    edges: typing.Dict[Vertex, int] = dataclasses.field(default_factory=dict)

    def __hash__(self) -> int:
        return self.i

    def __eq__(self, __value: object) -> bool:
        return self.i == __value

    def __repr__(self) -> str:
        return f'<V#{self.i}>'


@dataclasses.dataclass
class Graph:
    vertices: dict[int, Vertex] = dataclasses.field(default_factory=dict)

    def get_vertex(self, vid: int) -> Vertex:
        if vid not in self.vertices:
            self.vertices[vid] = Vertex(vid)
        return self.vertices[vid]


class IndexedPriorityQueue(typing.Generic[T]):
    """원소에 랜덤 엑세스가 가능하고 수정할 수 있는
    Binary Heap 기반의 Priority Queue
    """

    @dataclasses.dataclass
    class Node:
        priority: int
        data: T

        def __repr__(self) -> str:
            return self.data.__repr__()

    _heap: typing.List[Node] = []
    _indexed: typing.Dict[T, int] = {}

    def enqueue(self, data: T, priority: int):
        node = IndexedPriorityQueue.Node(priority, data)
        self._heap.append(node)
        self._indexed[data] = len(self._heap)-1
        self._siftdown(0, self._indexed[data])

    def dequeue(self) -> T:
        node = self._heap.pop()
        if self._heap:
            node, self._heap[0] = self._heap[0], node
            self._siftup(0)
        del self._indexed[node.data]
        return node.data

    def update(self, data: T, priority: int):
        index = self.indexof(data)
        self._heap[index].priority = priority
        self._siftup(index)
        self._siftdown(0, index)

    def indexof(self, data: T) -> int:
        return self._indexed[data]

    def empty(self) -> bool:
        return len(self._heap) == 0

    def _setitem(self, index: int, node: Node):
        self._heap[index] = node
        self._indexed[node.data] = index

    def _siftdown(self, startpos: int, pos: int):
        newitem = self._heap[pos]
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self._heap[parentpos]
            if newitem.priority < parent.priority:
                self._setitem(pos, parent)
                pos = parentpos
                continue
            break
        self._setitem(pos, newitem)

    def _siftup(self, pos: int):
        endpos = len(self._heap)
        startpos = pos
        newitem = self._heap[pos]
        childpos = 2*pos + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and not self._heap[childpos].priority < self._heap[rightpos].priority:
                childpos = rightpos
            self._setitem(pos, self._heap[childpos])
            pos = childpos
            childpos = 2*pos + 1
        self._setitem(pos, newitem)
        self._siftdown(startpos, pos)


def solve():
    """ Sparse 그래프에서, 우선순위 큐를 이용한 데이크스트라 알고리즘을 구현했으므로,
    최단경로 탐색에 걸리는 시간은 O( (E+V) log V )이다.

    참조: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        (Pseudocode - Running Time)

    E(문제에서 M)의 상한은 10,000이고, V(문제에서 N)의 상한은 1,000이다.
    전반적으로 동적할당을 사용하는 점을 무시하면 비교적 시간 복잡도 자체는 여유롭다.

    문제에서 왕복에 걸리는 시간(비용)을 구해야하는데,
    방향그래프 이므로, 가는 경로와 오는 경로가 다를 수 있다.

    오는 경로인 X번 정점에서 1..N번 정점으로 가는 최단거리는 dijkstra로 한번에 구할 수 있다.
    반대로, 가는 경로인 1...N번 정점에서 X번 정점에 대해서는, 단순하게 그래프의 방향을 역전해서 푸는 방식으로 접근했다.

    따라서 풀이의 시간 복잡도는 O(M + (N+M)logN), 즉 O((N+M)logN) 이다.
    """
    graph = Graph()
    graph_inv = Graph()
    N, M, X = map(int, sys.stdin.readline().split())
    for i in range(1, M+1):
        u, v, w = map(int, sys.stdin.readline().split())
        graph.get_vertex(u).edges[graph.get_vertex(v)] = w
        graph_inv.get_vertex(v).edges[graph_inv.get_vertex(u)] = w
    # 파티장으로 가는 거리
    dist = dijkstra(graph, graph.get_vertex(X))
    # 집으로 돌아오는 거리
    dist_inv = dijkstra(graph_inv, graph_inv.get_vertex(X))

    # 최대 왕복시간
    ans = 0
    for i in range(1,N+1):
        ans = max(ans, dist[i]+dist_inv[i])
    print(ans)


def dijkstra(graph: Graph, src: Vertex):
    """Dijkstra with modifiable priority queue

    Wiki 백과의 Pseudo 코드를 충실히 구현함.
    단, 최단 경로가 아닌 최단 거리만 구하므로, 경로를 기억하는 prev[]는 사용하지 않음.

    참조: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        (Pseudocode - Using a priority queue)
    """
    dist: typing.Dict[Vertex, int] = {}
    ipq: IndexedPriorityQueue[Vertex] = IndexedPriorityQueue()

    dist[src] = 0
    for v in graph.vertices.values():
        if v != src:
            dist[v] = sys.maxsize
        ipq.enqueue(v, dist[v])
    while not ipq.empty():
        u = ipq.dequeue()
        for v in u.edges:
            alt = dist[u] + u.edges[v]
            if alt < dist[v]:
                dist[v] = alt
                ipq.update(v, alt)
    return dist



if __name__ == "__main__":
    solve()
