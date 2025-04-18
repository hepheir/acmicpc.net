import sys


max_score = [0] * 3
min_score = [0] * 3
score = [0] * 3
buffer = [0] * 3


for n in range(int(sys.stdin.readline())):
    score[:] = map(int, sys.stdin.readline().split())

    buffer[0] = score[0] + max(max_score[:2])
    buffer[1] = score[1] + max(max_score)
    buffer[2] = score[2] + max(max_score[1:])
    max_score[:] = buffer[:]

    buffer[0] = score[0] + min(min_score[:2])
    buffer[1] = score[1] + min(min_score)
    buffer[2] = score[2] + min(min_score[1:])
    min_score[:] = buffer[:]


print(max(max_score), min(min_score))