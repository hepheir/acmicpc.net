# 18185번: 라면 사기 (Small)

from random import randint, choice
import sys


from Main import solve as solve_greedy
from bruteforce import solve as solve_bruteforce


sys.setrecursionlimit(int(10**8))
for i in range(1000):
    print(f'trying {i+1}th')
    N = 4
    A = [choice([0, 1, 2]) for _ in range(N)]
    B, C = 3, 2
    greedy = solve_greedy(A.copy(), B, C)
    bruteforce = solve_bruteforce(A.copy(), B, C)
    if greedy != bruteforce:
        print(N)
        print(*A)
        print('greedy:', greedy)
        print('bruteforce:', bruteforce)
        break
