QUESTS = [
    [
        [200, 210, 220],
        [210, 220, 225],
        [220, 225, 230],
        [225, 230, 235],
        [230, 235, 245],
        [235, 245, 250],
    ],
    [

        [260, 265, 270],
        [265, 270, 275],
        [270, 275, 280],
        [275, 280, 285],
        [280, 285, 290],
        [285, 290, 295],
        [290, 295, 300],
    ],
]


def solve(level: int, required_levels: list) -> int:
    if required_levels[0] <= level < required_levels[1]:
        return 500
    if required_levels[1] <= level < required_levels[2]:
        return 300
    if required_levels[2] <= level:
        return 100
    return 0


L = int(input())

for quests in QUESTS:
    print(*[solve(L, required_levels) for required_levels in quests])
