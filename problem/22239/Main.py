# 22239번: 가희와 읽기 쓰기 놀이 2

import sys
from typing import *
from collections import defaultdict

MAX_N = int(2e4)


def solve(n_players: int,
          n_cards: int,
          numbers: List[int],
          constraints: Dict[int, Tuple[int]],
          card_to_number: Dict[int, int]) -> str:
    number_to_cards = defaultdict(list)
    card_to_players = dict()
    for card in range(1, n_cards+1):
        number_to_cards[card_to_number[card]].append(card)
    for player in range(1, n_players+1):
        for card in constraints[player]:
            card_to_players[card] = player

    player_stack = {player: list(reversed(constraints[player])) for player in range(1, n_players+1)}
    stack = []

    def backtrack(i: int) -> bool:
        if i == n_cards:
            return True
        for card in number_to_cards[numbers[i]]:
            player = card_to_players[card]
            if not player_stack[player]:
                continue
            if player_stack[player][-1] != card:
                continue
            player_stack[player].pop()
            stack.append(player)
            if backtrack(i+1):
                return True
            stack.pop()
            player_stack[player].append(card)
        return False

    if not backtrack(0):
        return '-1'

    return ' '.join(map(str, stack))


def main():
    sys.setrecursionlimit(10*MAX_N+1000)
    N, C = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    constraints = {}
    card_to_number = {}
    for player in range(1, N+1):
        n_cards, *cards = map(int, sys.stdin.readline().split())
        constraints[player] = cards
    for card in range(1, C+1):
        card_to_number[card] = int(sys.stdin.readline().split()[1])
    answer = solve(N, C, numbers, constraints, card_to_number)
    print(answer)


if __name__ == '__main__':
    main()
