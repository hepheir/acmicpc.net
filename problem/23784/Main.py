# 23784번: Eidam-Sand Lair

import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        Yp, Lp, Ys, Ls = map(int, sys.stdin.readline().split())
        answer = solve(Yp, Lp, Ys, Ls)
        print(int(answer))


def solve(Yp: int, Lp: int, Ys: int, Ls: int) -> int:
    return min(
        Yp*Ys,                  # 처음부터 걸어감
        max(Lp, Yp+Yp-Lp)*Ls,   # 처음부터 엘리베이터 탑승
        abs(Yp-Lp)*Ys+Lp*Ls,    # 걸어서 내려간 후 엘리베이터 탑승
    )


if __name__ == '__main__':
    main()
