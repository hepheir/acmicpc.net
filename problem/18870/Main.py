# 18870번: 좌표 압축

N = int(input())
X = list(map(int, input().split()))
rank = [0] * N

index_ordered = sorted(range(N), key=lambda i: X[i])

rank[index_ordered[0]] = 0
prev_i = index_ordered[0]

for curr_i in index_ordered[1:]:
    if X[curr_i] == X[prev_i]:
        rank[curr_i] = rank[prev_i]
    else:
        rank[curr_i] = rank[prev_i] + 1
    prev_i = curr_i

print(*rank)
