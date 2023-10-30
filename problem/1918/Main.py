PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 3,
    ')': 3,
}


def is_operator(c: str) -> bool:
    return c in '+-*/()'


def solve():
    postfix = []
    stack = []
    for c in input().strip():
        if not is_operator(c):
            postfix.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while (top := stack.pop()) and top != '(':
                postfix.append(top)
        else:
            while stack and (stack[-1] != '(') and (PRECEDENCE[c] <= PRECEDENCE[stack[-1]]):
                postfix.append(stack.pop())
            stack.append(c)
    while stack:
        postfix.append(stack.pop())
    print(''.join(postfix))


if __name__ == "__main__":
    solve()