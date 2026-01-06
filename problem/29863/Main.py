# 29863번: Arno's Sleep Schedule

s = int(input())
if s < 20:
    s += 24

e = int(input())
e += 24

print(e-s)
