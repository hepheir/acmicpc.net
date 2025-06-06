def get_value(r: int, c: int) -> int:
    if r == 0 and c == 0:
        return 1
    radius = max(abs(r), abs(c))
    width = 2 * radius + 1
    offset = width ** 2
    if c == radius and r == radius:
        return offset
    if r == radius:
        return get_value(radius, radius) - radius + c
    if c == -radius:
        return get_value(radius, -radius) - radius + r
    if r == -radius:
        return get_value(-radius, -radius) - radius - c
    if c == radius:
        return get_value(-radius, radius) - radius - r
    raise ValueError


if __name__ == '__main__':
    r1, c1, r2, c2 = map(int, input().split())

    max_value = 0
    for r in range(r1, r2+1):
        max_value = max(max_value, get_value(r, c1))
        max_value = max(max_value, get_value(r, c2))
    for c in range(c1, c2+1):
        max_value = max(max_value, get_value(r1, c))
        max_value = max(max_value, get_value(r2, c))
    max_value_len = len(str(max_value))

    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            print(f'{get_value(r, c):{max_value_len}d}', end=' ')
        print()