import sys


def solve():
    C, N = map(int, sys.stdin.readline().split())
    cnames = set()
    unames = set()

    def can_win(gname: str) -> bool:
        for i in range(max(len(gname), 1000)):
            if gname[:i+1] in cnames:
                if gname[i+1:] in unames:
                    return True
        return False

    for _ in range(C):
        cname = sys.stdin.readline().rstrip()
        cnames.add(cname)
    for _ in range(N):
        uname = sys.stdin.readline().rstrip()
        unames.add(uname)
    Q = int(sys.stdin.readline())
    for _ in range(Q):
        gname = sys.stdin.readline().rstrip()
        if can_win(gname):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    solve()