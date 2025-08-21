# 19969번: Сборка компьютеров

# *1: VGA만 지원
# *2: DVI만 지원
# *3: VGA, DVI 모두 지원
# a*: 시스템 장치
# b*: 모니터
# c*: 연결된 장치 페어

a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

answer = 0

# 일단은 BGA, DVI 단일 포트들끼리 페어를 맺어본다.
c1 = min(a1, b1)
a1 -= c1
b1 -= c1

c2 = min(a2, b2)
a2 -= c2
b2 -= c2

answer += c1+c2

# BGA, DVI 단일 포트들을 상대의 범용 포트에 연결해준다.
c3_a = min(a3, b1+b2)
c3_b = min(b3, a1+a2)
a3 -= c3_a
b3 -= c3_b

answer += c3_a + c3_b

# 남는 범용 포트들끼리 연결해준다.
c3 = min(a3, b3)
a3 -= c3
b3 -= c3

answer += c3


print(answer)
