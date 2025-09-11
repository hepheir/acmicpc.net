# 9296번: Grading Exams

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for x in range(1, T+1):
        L = int(sys.stdin.readline())
        expect = sys.stdin.readline()
        actual = sys.stdin.readline()
        answer = 0
        for i in range(L):
            if expect[i] != actual[i]:
                answer += 1
        sys.stdout.write(f'Case {x}: {answer}\n')
