# 19969번: Сборка компьютеров

# *1: VGA만 지원
# *2: DVI만 지원
# *3: VGA, DVI 모두 지원
# a*: 시스템 장치
# b*: 모니터
# c*: 연결된 장치 페어

a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

# 일단은 1, 2, 3끼리 페어를 맺어본다.
c1 = min(a1, b1)
c2 = min(a2, b2)
c3 = min(a3, b3)

# 여분의 *3 계열 장치를 짝을 이루는 다른 기기와 맺어준다.
c_univ = min(a3-c3, b1-c1+b2-c2) + min(b3-c3, a1-c1+a2-c2)

print(c1 + c2 + c3 + c_univ)
