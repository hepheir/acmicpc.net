# 사탕 묶음에 들어갈 수 있는 최대 수가 1000 이므로,
# 나올 수 없는 수인 1001을 infinity 를 의미하는 수로 사용.
INF = 1001


ans = 0 # 가져갈 사탕의 개수

# 홀수 개의 사탕을 가진 사탕 묶음...
min_odd = INF # ...중에서 가장 적은 수의 사탕을 가진 사탕 묶음 속 사탕의 개수
n_odds = 0 # ...의 개수

# 사탕 묶음의 개수는 필요 없으므로 버림
input()

# 각 사탕 묶음 속 사탕의 개수 a에 대해 살펴본다.
for a in map(int, input().split()):
    if a % 2 == 1:
        n_odds += 1
        # 홀수개의 사탕 중 가장 작은 것을 찾음
        if a < min_odd:
            min_odd = a
    ans += a # 일단은 모든 사탕을 가져간다고 전제.


# 홀수개의 사탕 묶음이 홀수 개이면, 짝수개로 짝수를 만들고 남은 나머지 하나만 버리면 됨.
if n_odds % 2 == 1 and min_odd != INF:
    ans -= min_odd


print(ans)