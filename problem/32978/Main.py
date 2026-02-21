# 32978번: 아 맞다 마늘

N = int(input())
A = set(input().split())
B = set(input().split())

print(*(A - B))
