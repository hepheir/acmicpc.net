# 27544번: コイン集め 2 (Coin Collecting 2)

import sys


FACE_UP = '#'
FACE_DN = '.'


H, W = map(int, sys.stdin.readline().split())
S = [sys.stdin.readline().strip() for _ in range(H)]

COL_FACE_UP_COUNT = [0] * W
ROW_FACE_UP_COUNT = [0] * H
DEFAULT_AOI_SCORE = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == FACE_UP:
            ROW_FACE_UP_COUNT[i] += 1
            COL_FACE_UP_COUNT[j] += 1
            DEFAULT_AOI_SCORE += 1


def best_score_of_aoi() -> int:
    max_aoi_score = -1
    for i in range(H):
        rin_score = best_score_of_rin(i)
        aoi_score = H*W - rin_score
        if max_aoi_score < aoi_score:
            max_aoi_score = aoi_score
    return max_aoi_score


def best_score_of_rin(i: int) -> int:
    max_rin_score = -1
    for j in range(W):
        aoi_score = calc_aoi_score(i, j)
        rin_score = H*W - aoi_score
        if max_rin_score < rin_score:
            max_rin_score = rin_score
    return max_rin_score


def calc_aoi_score(i: int, j: int) -> int:
    # 아오이가 i행, 린이 j열을 뒤집었을 때, 아오이의 점수.

    aoi_score = DEFAULT_AOI_SCORE

    # 아오이가 먼저 뒤집는다.
    aoi_score -= ROW_FACE_UP_COUNT[i]  # 선택한 행의 기존 점수를 빼주고
    aoi_score += H-ROW_FACE_UP_COUNT[i]  # 갱신된 후의 점수를 더해준다.

    # 린이 앞으로 뒤집을 열(col)중 한 칸은 아오이에 의해 뒤집힌 점을 보정.
    score_adjust = 1 if (S[i][j] == FACE_UP) else -1

    # 린이 뒤집는다.
    aoi_score -= (COL_FACE_UP_COUNT[j] - score_adjust)
    aoi_score += W-(COL_FACE_UP_COUNT[j] - score_adjust)

    return aoi_score


aoi_score = best_score_of_aoi()
rin_score = H*W - aoi_score

sys.stdout.write(f"{aoi_score} {rin_score}\n")
