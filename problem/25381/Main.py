import sys


S = sys.stdin.readline().strip()

pos = {
    'A': [],
    'B': [],
    'C': [],
}

for i in reversed(range(len(S))):
    pos[S[i]].append(i)


answer = 0

while pos['B'] and pos['C']:
    if pos['B'][-1] < pos['C'][-1]:
        pos['B'].pop()
        pos['C'].pop()
        answer += 1
    else:
        pos['C'].pop()


while pos['A'] and pos['B']:
    if pos['A'][-1] < pos['B'][-1]:
        pos['A'].pop()
        pos['B'].pop()
        answer += 1
    else:
        pos['B'].pop()

print(answer)
