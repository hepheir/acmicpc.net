# 1284번: 집 주소

import sys


def main():
    while (N := sys.stdin.readline().strip()) != '0':
        answer = len(N)+1
        for c in N:
            if c == '0':
                answer += 4
                continue
            if c == '1':
                answer += 2
                continue
            answer += 3
        print(answer)


if __name__ == '__main__':
    main()
