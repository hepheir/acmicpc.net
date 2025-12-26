# 17245번: 서버실

import bisect
import sys


N = int(sys.stdin.readline())

server_rack = []
for y in range(N):
    server_rack.extend(map(int, sys.stdin.readline().split()))
server_rack.sort()

server_rack_height_ps = server_rack.copy()
for i in range(1, len(server_rack)):
    server_rack_height_ps[i] += server_rack_height_ps[i-1]
server_rack_height_ps.append(0)  # zero-padding for -1 index.

n_servers = sum(server_rack)


def n_available_servers(t: int) -> int:
    n_leq_racks = bisect.bisect_right(server_rack, t)
    n_gt_racks = len(server_rack)-n_leq_racks
    return server_rack_height_ps[n_leq_racks-1] + t*n_gt_racks


lo = 0
hi = max(server_rack)
while lo < hi:
    mid = (lo + hi) // 2
    if n_available_servers(mid) >= (0.5 * n_servers):
        hi = mid
    else:
        lo = mid + 1

print(lo)
