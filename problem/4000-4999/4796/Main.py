import sys


def solve() -> None:
    tc_no = 1 # 테스트케이스 번호
    while (line := sys.stdin.readline().rstrip()) != '0 0 0':
        L, P, V = map(int, line.split())
        # 휴가 기간(V) 중, 연속하는 기간(P) 주기를 세면, 그 중 L일을 사용가능 하므로, "L * (V // P)" 의식으로 사용가능한 날짜를 셀 수 있다.
        # 휴가 기간의 막바지에서 P 기간을 완전히 채우지 못하였을 때, 사용가능한 날을 "min(V % P, L)" 을 통해서 구한다.
        ans = L * (V // P) + min(V % P, L)
        sys.stdout.write(f'Case {tc_no}: {ans}\n')
        tc_no += 1


if __name__ == "__main__":
    solve()
