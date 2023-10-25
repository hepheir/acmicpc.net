import sys

while (line := sys.stdin.readline().strip()) != "# 0 0":
    name, age, weight = line.split()
    print(name, end=' ')
    if int(age) > 17 or int(weight) >= 80:
        print('Senior')
    else:
        print('Junior')