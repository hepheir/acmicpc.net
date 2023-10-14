def solve():
    L, R = input().split()
    ans = 0
    if len(L) == len(R):
        for i in range(len(L)):
            if L[i] != R[i]:
                break
            if L[i] == '8':
                ans += 1
    print(ans)


if __name__ == "__main__":
    solve()