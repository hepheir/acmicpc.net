# 17488번: 수강 바구니

from typing import Dict, List, Set
import sys


def sugang(students: Set[int],
           lectures: Set[int],
           lecture_capacity: Dict[int, int],
           student_lectures: Dict[int, List[int]],
           student_carts: Dict[int, List[int]]):
    lecture_students: Dict[int, List[int]] = {lecture_id: [] for lecture_id in range(1, M+1)}
    for student_id in students:
        for lecture_id in student_carts[student_id]:
            lecture_students[lecture_id].append(student_id)
    for lecture_id in lectures:
        lecture_capacity[lecture_id] -= len(lecture_students[lecture_id])
        if lecture_capacity[lecture_id] < 0:
            continue
        for student_id in lecture_students[lecture_id]:
            student_lectures[student_id].append(lecture_id)


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    L = [None] + [*map(int, sys.stdin.readline().split())]

    students = set(range(1, N+1))
    lectures = set(range(1, M+1))

    student_lectures: Dict[int, List[int]] = {student_id: [] for student_id in range(1, N+1)}

    for _ in range(2):
        student_carts: Dict[int, List[int]] = {student_id: [] for student_id in range(1, N+1)}
        for student_id in range(1, N+1):
            for lecture_id in map(int, sys.stdin.readline().split()):
                if lecture_id == -1:
                    break
                student_carts[student_id].append(lecture_id)
        sugang(students, lectures, L, student_lectures, student_carts)

    for student_id in range(1, N+1):
        student_lectures[student_id].sort()
        if not student_lectures[student_id]:
            sys.stdout.write(f'망했어요\n')
        else:
            sys.stdout.write(' '.join(map(str, student_lectures[student_id]))+'\n')
