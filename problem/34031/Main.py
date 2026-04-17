# 34031번: 하이터치☆메모리


A = input()
B = input()


def count_over_open(S: str):
    stack = []
    for c in S:
        if c == '(':
            stack.append(c)
        elif stack:
            stack.pop()
        else:
            return
        yield len(stack)


def count_over_close(S: str):
    stack = []
    count = 0
    for c in S:
        if c == '(':
            stack.append(c)
        elif stack:
            stack.pop()
        else:
            count += 1
        if not stack:
            yield count


open_counter = [0] * (len(A)+1)
for count in count_over_open(A):
    open_counter[count] += 1

close_counter = [0] * (len(B)+1)
for count in count_over_close(B):
    close_counter[count] += 1

answer = 0
for n in range(min(len(A), len(B))+1):
    answer += open_counter[n] * close_counter[n]

print(answer)
