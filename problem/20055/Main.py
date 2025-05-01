import sys
from collections import deque
from dataclasses import dataclass
from typing import Deque, List


N, K = map(int, sys.stdin.readline().split())


nodes_durability = [*map(int, sys.stdin.readline().split())]
nodes_is_empty = [True] * (2*N)

node_enter = 0
node_exit = N-1


def prev_node(node: int) -> int:
    return (node-1) % (2*N)


def count_dead_nodes() -> int:
    return sum([1 for durability in nodes_durability if durability == 0])


def on_state_update():
    nodes_is_empty[node_exit] = True


def rotate_all_nodes():
    global node_enter, node_exit
    node_enter = prev_node(node_enter)
    node_exit = prev_node(node_exit)
    nodes_is_empty[node_exit] = True


def move_all_robots():
    node = node_exit
    while node != node_enter:
        # move robot <prev node> -> <node>
        if not nodes_is_empty[prev_node(node)] and nodes_is_empty[node] and nodes_durability[node] > 0:
            nodes_is_empty[prev_node(node)] = True
            nodes_is_empty[node] = False
            nodes_durability[node] -= 1
        node = prev_node(node)
    nodes_is_empty[node_exit] = True


def try_put_robot():
    node = node_enter
    if nodes_durability[node] > 0:
        nodes_is_empty[node] = False
        nodes_durability[node] -= 1


steps = 0
while count_dead_nodes() < K:
    steps += 1
    rotate_all_nodes()
    move_all_robots()
    try_put_robot()

print(steps)
