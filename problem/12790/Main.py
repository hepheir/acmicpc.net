# 12790번: Mini Fantasy War

import sys


T = int(sys.stdin.readline())
for _ in range(T):
    c_hp, c_mp, c_atk, c_def, e_hp, e_mp, e_atk, e_def = map(int, sys.stdin.readline().split())
    power = max(c_hp+e_hp, 1)+5*max(c_mp+e_mp, 1)+2*max(c_atk+e_atk, 0)+2*(c_def+e_def)
    print(power)
