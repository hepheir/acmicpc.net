from collections import defaultdict
import sys


READ = defaultdict(int)
WRITE = defaultdict(int)

time = 1
last_wait = 0


def exec_READ(A: int):
    global time
    # check READ with WRITE
    if WRITE[A] > last_wait:
        exec_WAIT()
    READ[A] = time
    sys.stdout.write(f'READ {A}\n')
    time += 1


def exec_WRITE(A: int, B: int):
    global time
    # check READ with WRITE
    if READ[B] > last_wait:
        exec_WAIT()
    # check WRITE with WRITE
    if WRITE[A] > last_wait:
        exec_WAIT()
    if WRITE[B] > last_wait:
        exec_WAIT()
    READ[A] = time
    WRITE[B] = time
    sys.stdout.write(f'WRITE {A} TO {B}\n')
    time += 1


def exec_WAIT():
    global last_wait, time
    last_wait = time
    sys.stdout.write('WAIT\n')
    time += 1


def exec_EXIT():
    global time
    sys.stdout.write('EXIT\n')
    time += 1


while True:
    stmt = sys.stdin.readline().strip()
    tokens = stmt.split()
    if tokens[0] == 'READ':
        A = tokens[1]
        exec_READ(A)
        continue
    if tokens[0] == 'WRITE':
        A = tokens[1]
        B = tokens[3]
        exec_WRITE(A, B)
        continue
    if tokens[0] == 'EXIT':
        exec_EXIT()
        break
