# 3603번: Journey with Pigs

import sys


n, t = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))
p = list(map(int, sys.stdin.readline().split()))

# 돼지의 실제 판매 이윤은 판매액-운송비이다.
# 이를 반영한 마을 별 돼지 가격표를 생성한다.
village_profit_per_kilogram = [(p[j]-d[j]*t) for j in range(n)]

# 이윤이 적게 나는 곳에 무게가 적은 돼지를 판다.
village_id_list = list(range(n))
pig_id_list = list(range(n))

village_id_list.sort(key=lambda j: village_profit_per_kilogram[j])
pig_id_list.sort(key=lambda i: w[i])

answer = [None] * n  # 어느 마을에 몇 번째 돼지를 팔 지.
for village_id, pig_id in zip(village_id_list, pig_id_list):
    answer[village_id] = pig_id+1  # zero-base -> one-base

print(*answer)
