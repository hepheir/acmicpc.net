TOYCARTOON = 'toycartoon'


def main():
    S = input().strip()
    print(solve(S))


def solve(S: str) -> str:
    T, O, Y = split_TOY(S)
    if not O:
        name = TOYCARTOON+'_'+S
    else:
        Y = remove_redundant_prefix(S, O, Y)
        name = T+S+Y
    if len(name) > 20:
        return TOYCARTOON
    return name


def split_TOY(S: str):
    for length in reversed(range(1, len(S)+1)):
        s = S[:length]
        if s in TOYCARTOON:
            i = TOYCARTOON.index(s)
            T = TOYCARTOON[:i]
            O = s
            Y = TOYCARTOON[i+length:]
            return T, O, Y
    T = TOYCARTOON
    O = ''
    Y = ''
    return T, O, Y


def remove_redundant_prefix(S: str, O: str, Y: str) -> str:
    # S에서 O를 제외한 부분
    s = S.lstrip(O)
    # s의 접미사이면서 Y의 접두사인 가장 긴 문자열을 지운 것
    for length in reversed(range(1, len(Y)+1)):
        y = Y[:length]
        if s.endswith(y):
            return Y[length:]
    return Y


if __name__ == '__main__':
    main()
