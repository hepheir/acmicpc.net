# 1417번: 국회의원 선거

import sys


N = int(sys.stdin.readline())
my_votes, *other_votes = (int(sys.stdin.readline()) for _ in range(N))
answer = 0

while (votes := max(other_votes, default=0)) >= my_votes:
    i = other_votes.index(votes)
    other_votes[i] -= 1
    my_votes += 1
    answer += 1

print(answer)
