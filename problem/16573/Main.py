# 16573번: Edit Distance


S = input().strip()
count = {
    '0': 0,
    '1': 0,
}
for c in S:
    count[c] += 1

T = S.replace('0', '1') if (count['0'] > count['1']) else S.replace('1', '0')
print(T)
