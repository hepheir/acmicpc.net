# 28113번: 정보섬의 대중교통

N, A, B = map(int, input().split())

if A < B:
    print('Bus')
elif B < N:
    print('Bus')
elif A > B:
    print('Subway')
else:
    print('Anything')
