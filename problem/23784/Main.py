# 23784번: Eidam-Sand Lair

import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        Yp, Lp, Ys, Ls = map(int, sys.stdin.readline().split())
        answer = solve(Yp, Lp, Ys, Ls)
        print(int(answer))


def solve(Yp: int, Lp: int, Ys: int, Ls: int) -> int:
    if Ys <= Ls:
        return Yp*Ys

    def take_ev_at(f: int) -> int:
        return max(abs(Yp-f)*Ys, abs(Lp-f)*Ls) + abs(f)*Ls

    # 경사 하강법...
    lo = 0
    hi = Yp
    while lo < hi:
        mid = (lo+hi)//2
        df = take_ev_at(mid)-take_ev_at(mid-1)
        if df <= 0:
            lo = mid+1
        else:
            hi = mid-1

    return min(
        # 처음 층부터 걸어 올라가는 시간
        Yp*Ys,
        # 처음 층에서 엘리베이터를 누르고 기다리는 시간
        abs(Yp-Lp)*Ls+Yp*Ls,
        # 어느정도 걸어 올라간 뒤에 엘베 호출
        take_ev_at(lo-1),
        take_ev_at(lo),
        take_ev_at(lo+1),
    )


if __name__ == '__main__':
    main()
