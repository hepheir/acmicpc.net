import sys


def solve(N: int, C: int, X: list[int]):
    X.sort()
    def is_possible(dist):
        count = 1
        prev = X[0]
        for i in range(1, N):
            if X[i]-prev < dist:
                continue
            count += 1
            prev = X[i]
        return count >= C
    lo = 1
    hi = X[-1]-X[0]
    ans = 0
    while lo <= hi:
        mid = (lo+hi)//2
        if is_possible(mid):
            lo = mid+1
            ans = mid
        else:
            hi = mid-1
    print(ans)
    return


if __name__ == "__main__":
    N, C = map(int, sys.stdin.readline().split())
    X = list(map(int, sys.stdin.readlines()))
    solve(N, C, X)
