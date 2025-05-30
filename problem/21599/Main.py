N = int(input())
A = sorted(map(int, input().split()), reverse=True)

did_upgrade = [0] * N

to_upgrade = 0
for i in range(N):
    # TODO: 자기 자신도 강화대상에 포함되는지 확인하기
    if to_upgrade < A[i]:
        to_upgrade = A[i]
    if to_upgrade:
        did_upgrade[i] = 1
        to_upgrade -= 1

for i in range(to_upgrade):
    if did_upgrade[i] == 0:
        did_upgrade[i] = 1

print(sum(did_upgrade))
