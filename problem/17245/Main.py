# 17245번: 서버실

import bisect
import sys


N = int(sys.stdin.readline())

server_rack = []
for y in range(N):
    server_rack.extend(map(int, sys.stdin.readline().split()))
server_rack.sort()


def n_available_servers(t: int) -> int:
    n_leq_racks = bisect.bisect_right(server_rack, t)
    n_gt_racks = len(server_rack)-n_leq_racks
    return sum(server_rack[:n_leq_racks]) + t*n_gt_racks


lo = 0
hi = max(server_rack)
while lo < hi:
    mid = (lo + hi) // 2
    if n_available_servers(mid) >= (0.5 * sum(server_rack)):
        hi = mid
    else:
        lo = mid + 1

print(lo)
