# 23784번: Eidam-Sand Lair

from math import ceil
import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        Yp, Lp, Ys, Ls = map(int, sys.stdin.readline().split())
        answer = solve(Yp, Lp, Ys, Ls)
        print(int(answer))


def solve(Yp: float, Lp: int, Ys: int, Ls: int) -> float:
    if Yp == Lp:
        return Yp * min(Ys, Ls)
    if Yp == 0:
        return 0
    Ld = ceil(Yp) - Lp
    Lt = abs(Ld) * Ls
    if Yp * Ys <= Lt:
        # 걸어 올라가는게 낫다.
        answer = Yp * Ys
    elif Ys > Lt+Ls:
        # 기다리는게 낫다.
        answer = solve(ceil(Yp), Lp+Ld, Ys, Ls) + Lt
    else:
        # 엘리베이터가 Yp로 올 동안 걸어 올라가자.
        answer = solve(Yp - Lt / Ys, Lp + Ld, Ys, Ls) + Lt
    return answer


if __name__ == '__main__':
    main()
