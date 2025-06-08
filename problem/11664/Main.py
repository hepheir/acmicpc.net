Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, input().split())


def dot(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    return x1*x2+y1*y2+z1*z2


def l2_norm(x: float, y: float, z: float) -> float:
    return (x*x+y*y+z*z) ** 0.5


def face_to_point_dist(px, py, pz) -> float:
    # 평면의 법선 벡터
    vx = Ax - Bx
    vy = Ay - By
    vz = Az - Bz
    # 평면(위 임의의 점)으로 부터 점으로의 방향 벡터
    wx = Cx - px
    wy = Cy - py
    wz = Cz - pz
    # D = |v \dot w| / |v|
    return abs(dot(vx, vy, vz, wx, wy, wz)) / l2_norm(vx, vy, vz)


def face_determinator(x: float, y: float, z: float) -> float:
    # 평면의 방정식의 판별식
    return (Ax-Bx)*(x-Cx) + (Ay-By)*(y-Cy) + (Az-Bz)*(z-Cz)


def does_line_pierce_face() -> bool:
    # 판별식 부호가 다르거나, 둘 중 하나라도 0이면 접하거나 지나가긴 한다.
    a_det = face_determinator(Ax, Ay, Az)
    b_det = face_determinator(Bx, By, Bz)
    return a_det * b_det <= 0


if does_line_pierce_face():
    # Case 1: 선분이 평면에 접해있는 경우.
    # 점과 선분-평면의 접점 사이의 거리를 구한다.
    # a:b는 평면과 선분의 양 끝점 사이의 거리의 비율이다.
    a = face_to_point_dist(Ax, Ay, Az)
    b = face_to_point_dist(Bx, By, Bz)
    # 평면과 선분의 교점을 구한다. (대칭비 이용)
    x = (Ax*b+Bx*a) / (a+b)
    y = (Ay*b+By*a) / (a+b)
    z = (Az*b+Bz*a) / (a+b)
    answer = l2_norm(Cx-x, Cy-y, Cz-z)
else:
    # Case 2: 선분이 평면을 통과하지 않는 경우.
    # 점과 선분의 양 끝중 가까운 것과의 거리를 구한다.
    answer = min(
        l2_norm(Cx-Ax, Cy-Ay, Cz-Az),
        l2_norm(Cx-Bx, Cy-By, Cz-Bz),
    )

print(f'{answer:.10f}')
