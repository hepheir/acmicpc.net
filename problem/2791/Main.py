# 2791번: KONCERT

import sys


GUY_COUNT, _ = map(int, sys.stdin.readline().split())
GUYS_WITH_TICKET = tuple(map(int, sys.stdin.readline().split()))

GIRL_COUNT, _ = map(int, sys.stdin.readline().split())
GIRLS_WITH_TICKET = tuple(map(int, sys.stdin.readline().split()))

# --------------------------------
# 티켓을 가지고 있는 남자는 바로 입장시킨다.
# --------------------------------

for guy in GUYS_WITH_TICKET:
    sys.stdout.write(f'ENTER GUY {guy}\n')

guy_inside = list(GUYS_WITH_TICKET)
guy_outside = list(set(range(1, GUY_COUNT+1)) - set(guy_inside))

# --------------------------------
# 한 명의 운송책이 될 여자를 남겨두고, 그 외 모든 여자들의 티켓을 남자들에게 양도한다.
# --------------------------------

girl_outside = list(GIRLS_WITH_TICKET)
while len(girl_outside) > 1 and guy_outside:
    girl = girl_outside.pop()
    guy = guy_outside.pop()
    guy_inside.append(guy)
    sys.stdout.write(f'GIVE GIRL {girl} GUY {guy}\n')
    sys.stdout.write(f'ENTER GUY {guy}\n')

# --------------------------------
# 운송책이 티켓을 나르며 최대한 많은 남자들을 입장시킨다.
# --------------------------------

girl = girl_outside.pop()  # 운송책
while guy_outside:
    if guy_inside and len(guy_outside) > 1:
        # 입장한 사람들의 티켓을 몰래 빼돌리자.
        ticket_count = min(len(guy_inside), len(guy_outside))
        sys.stdout.write(f'ENTER GIRL {girl}\n')
        for _ in range(ticket_count):
            sys.stdout.write(f'GIVE GUY {guy_inside.pop()} GIRL {girl}\n')
        sys.stdout.write(f'EXIT GIRL {girl}\n')
        for _ in range(ticket_count):
            guy = guy_outside.pop()
            sys.stdout.write(f'GIVE GIRL {girl} GUY {guy}\n')
            sys.stdout.write(f'ENTER GUY {guy}\n')
            guy_inside.append(guy)
    else:
        # 이 한 명의 남자가 입장 가능한 최후의 1인이다.
        guy = guy_outside.pop()
        sys.stdout.write(f'GIVE GIRL {girl} GUY {guy}\n')
        sys.stdout.write(f'ENTER GUY {guy}\n')
