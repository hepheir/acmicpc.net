# 24736번: Football Scoring

def scoring(T: int, F: int, S: int, P: int, C: int):
    return 6*T + 3*F + 2*S + 1*P + 2*C


print(scoring(*map(int, input().split())), scoring(*map(int, input().split())))
