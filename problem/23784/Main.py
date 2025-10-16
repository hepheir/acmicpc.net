# 23784번: Eidam-Sand Lair

from math import ceil, floor
import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        Yp, Lp, Ys, Ls = map(int, sys.stdin.readline().split())
        answer = solve(Yp, Lp, Ys, Ls)
        print(int(answer))


def solve(Yp: int, Lp: int, Ys: int, Ls: int) -> float:
    # x층에서 엘리베이터를 탑승한다고 하면, 최적의 탑승 위치 x는...
    # abs(Yp-x)*Ys = abs(Lp-x)*Ls
    # (Yp^2 - 2*x*Yp + x^2) * Ys^2 = (Lp^2 - 2*x*Lp + x^2) * Ls^2
    # x^2*(Ys^2 - Ls^2) + 2*x*(Lp*Ls^2 - Yp*Ys^2) + Yp^2*Ys^2 - Lp^2*Ls^2 = 0
    x_candidates = []
    if Ys-Ls != 0:
        x = (Yp*Ys-Lp*Ls)/(Ys-Ls)
        if 0 <= x <= max(Yp, Lp):
            x_candidates.append(ceil(x))
            x_candidates.append(floor(x))
    if Ys+Ls != 0:
        x = (Yp*Ys+Lp*Ls)/(Ys+Ls)
        if 0 <= x <= max(Yp, Lp):
            x_candidates.append(ceil(x))
            x_candidates.append(floor(x))
    ans_candidates = [
        Yp*Ys,
        calc_time(Yp, Lp, Ys, Ls, 0),
        calc_time(Yp, Lp, Ys, Ls, Yp),
        calc_time(Yp, Lp, Ys, Ls, Lp),
        *(calc_time(Yp, Lp, Ys, Ls, x) for x in x_candidates),
    ]
    return min(ans_candidates)


def calc_time(Yp: int, Lp: int, Ys: int, Ls: int, x: int) -> int:
    """x층에서 엘리베이터를 타고 가면 걸리는 시간"""
    return max(abs(Yp-x)*Ys, abs(Lp-x)*Ls) + x*Ls


if __name__ == '__main__':
    main()
