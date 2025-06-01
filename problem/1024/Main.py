N, L = map(int, input().split())


for l in range(L, 100+1):
    # 합이 N이면서 길이가 l인 직선이 존재하는지 검사하기.

    # 등차수열의 합 공식을 사용:
    # 시작값: s, 종료값: e. (단, e = s+l-1)
    # (수열의 합) = (e-s+1) * (s+e)/2
    #             = ((s+l-1)-s+1) * (s+(s+l-1)) / 2
    #             = l * (2s+l-1) / 2
    #             = N
    # l * (2s+l-1) / 2  = N
    # l * (2s+l-1)      = 2N
    # 2s+l-1            = 2N / l
    # 2s                = (2N / l)-l+1
    # s                 = ((2N / l)-l+1) / 2
    #                   = ((2N / l)-(l^2 / l)+(l / l)) / 2
    #                   = ((2N-l^2+l) / l) / 2
    #                   = (2N-l^2+l) / 2l

    numerator = 2*N-l*l+l
    denominator = 2*l

    if numerator % denominator != 0:
        # 시작 값이 정수가 아님.
        continue

    if (s := numerator // denominator) < 0:
        # 시작 값이 음이 아닌 정수가 아님.
        continue

    # 정답을 찾음.
    print(*[x for x in range(s, s+l)])
    break
else:
    # 정답을 찾지 못함.
    print(-1)
