digits = list(map(int, input()))
digits.reverse()

for i in range(len(digits)-1):
    if digits[i] >= 5:
        digits[i+1] += 1
    digits[i] = 0

print(''.join(map(str, reversed(digits))))