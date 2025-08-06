# 32466번: Jenga Game

import sys


# 직접 출력해서 패턴을 찍어보니 무언가가 보였다...
# def can_win(b_011: int, b_111: int) -> bool:
#     if b_111 > 0:
#         if not can_win(b_011, b_111-1):
#             return True
#         if not can_win(b_011+1, b_111-1):
#             return True
#     if b_011 > 0:
#         if not can_win(b_011-1, b_111):
#             return True
#     return False


def can_win(b_011: int, b_111: int) -> bool:
    if b_011 % 2:
        return True
    return b_111 % 2


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    # 아래 이외의 경우는 이미 한 블록이라도 빼는 순간 불안정해지는 상태이다.
    b_011 = 0
    b_111 = 0
    sys.stdin.readline().strip() # top layer must not be touched
    for i in range(N-1):
        row = sys.stdin.readline().strip()
        if row == '011' or row == '110':
            b_011 += 1
        if row == '111':
            b_111 += 1
    if can_win(b_011, b_111):
        sys.stdout.write(f"Yesyes\n")
    else:
        sys.stdout.write(f"Nono\n")