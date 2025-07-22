# 30191번: 문자열 만들기 1

APPEND_SU = 'S'
MV_CURSOR = 'N'
APPEND_US = 'U'

N = int(input())
T = input().strip()

stack = []
moves = []
i = N-1
while i > len(stack):
    if stack and stack[-1] == T[i]:
        moves.append(MV_CURSOR)
        stack.pop()
        i -= 1
    elif T[i] == 'S':
        moves.append(APPEND_US)
        stack.append('U')
        stack.append('S')
    else:
        moves.append(APPEND_SU)
        stack.append('S')
        stack.append('U')

print(len(moves))
print(''.join(moves))
