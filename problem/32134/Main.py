def estimate_force(f: float, A: float, B: float, C: float, D: float) -> float:
    return 0.5*((A-D)+(B-C))*f



def estimate_force_all(N: int, f: list, A_1: float, B_N: float, D_1: float, C_N: float) -> float:
    def p(i: int) -> float:
        return (N-(i-1)) / (N)

    def q(i: int) -> float:
        return 1 - p(i)

    force = 0
    for i in range(1, N+1):
        D_i = p(i) * D_1 + q(i) * C_N
        C_i = p(i+1) * D_1 + q(i+1) * C_N
        force += estimate_force(f[i], A_1, B_N, D_i, C_i)
    return force


if __name__ == '__main__':
    N, H, S = map(int, input().split())
    f = [None, *map(int, input().split())]

    f_sum_l = 0
    f_sum_r = 0
    l = 1
    r = N
    while l < r:
        f_sum_l += f[l]
        f_sum_r += f[r]
        l += 1
        r -= 1

    hi = min(H, 2*(S/N))
    lo = 2*(S/N) - hi
    while (lo+0.00001) < hi:
        mid = 0.5*(lo+hi)
        if (0.5*(lo+hi))*N < S:
            lo = mid+1
        else:
            hi = mid

    len_min = lo
    len_max = 2 * (S / N) - lo

    if f_sum_l < f_sum_r:
        answer = estimate_force_all(N, f, A_1=H, B_N=H, C_N=H-len_min, D_1=H-len_max)
    else:
        answer = estimate_force_all(N, f, A_1=H, B_N=H, C_N=H-len_max, D_1=H-len_min)

    print(f'{answer:0.6f}')
