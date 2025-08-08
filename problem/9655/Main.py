# 돌 게임

MAX_N = 1000

# 모든 플레이어가 완벽하게 플레이 할 경우, = "상대가 이길 여지를 주지 않는게 포인트."
# 돌이 N개 있을 때, 지금 턴에 해당하는 플레이어가 이길 수 있는가?

# STONE_GAME[N] -> 돌이 N개 있을 때, 현재 플레이어가 완벽하게 이길 수 있는가?
STONE_GAME = [True] * (MAX_N+1)
STONE_GAME[0] = False

for n in range(MAX_N+1):
    STONE_GAME[n] = (not STONE_GAME[n-1]) or (not STONE_GAME[n-3])


if __name__ == '__main__':
    N = int(input())
    if STONE_GAME[N]:
        print('SK')
    else:
        print('CY')
