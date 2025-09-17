# 16573번: Edit Distance


INV = {'0': '1', '1': '0', }

S = input().strip()
N = len(S)

count = {'0': 0, '1': 0, }
for c in S:
    count[c] += 1

if count['0'] == count['1']:
    T = INV[S[0]] + S[0]*(N-1)
else:
    T = min(count, key=lambda k: count[k]) * N

print(T)
