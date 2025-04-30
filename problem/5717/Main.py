import sys


while True:
    M, F = map(int, sys.stdin.readline().split())

    if M == 0 and F == 0:
        break

    sys.stdout.write(f'{M+F}\n')
