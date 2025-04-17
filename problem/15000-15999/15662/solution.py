import sys


MAX_T = 1000
sys.setrecursionlimit(10*MAX_T)

T = int(sys.stdin.readline())

gear_tooth = [sys.stdin.readline().strip() for _ in range(T)]
gear_pivot = [0] * T
gear_age = [-1] * T


def get_l_tooth(gear_id: int) -> str:
    return gear_tooth[gear_id][(gear_pivot[gear_id]-2) % 8]


def get_r_tooth(gear_id: int) -> str:
    return gear_tooth[gear_id][(gear_pivot[gear_id]+2) % 8]


def get_t_tooth(gear_id: int) -> str:
    return gear_tooth[gear_id][gear_pivot[gear_id]]


def should_propagate_l(gear_id: int) -> bool:
    if gear_id-1 < 0:
        return False
    if get_r_tooth(gear_id-1) == get_l_tooth(gear_id):
        return False
    if gear_age[gear_id-1] >= gear_age[gear_id]:
        return False
    return True


def should_propagate_r(gear_id: int) -> bool:
    if gear_id+1 >= T:
        return False
    if get_r_tooth(gear_id) == get_l_tooth(gear_id+1):
        return False
    if gear_age[gear_id+1] >= gear_age[gear_id]:
        return False
    return True


def rotate(gear_id: int, clockwise: bool, age: int) -> None:
    gear_age[gear_id] = age
    if should_propagate_l(gear_id):
        rotate(gear_id-1, not clockwise, age)
    if should_propagate_r(gear_id):
        rotate(gear_id+1, not clockwise, age)
    if clockwise:
        gear_pivot[gear_id] = (gear_pivot[gear_id]-1) % 8
    else:
        gear_pivot[gear_id] = (gear_pivot[gear_id]+1) % 8


K = int(sys.stdin.readline())
for age in range(K):
    args = [*map(int, sys.stdin.readline().split())]
    rotate(gear_id=args[0]-1, clockwise=(args[1] == 1), age=age)
    pass

answer = 0
for gear_id in range(T):
    if get_t_tooth(gear_id) == '1':
        answer += 1

print(answer)
