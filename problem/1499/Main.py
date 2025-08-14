# 1499번: 뒤집기 수열

A = list(input().strip())
B = list(input().strip())
N = len(A)

swap_count = 0
i = 0
j = N-1
while i <= j:
    while i < j and A[j] == B[j]:
        j -= 1
    if A[i] != B[i]:
        for k in reversed(range(i+1, j+1)):
            if A[k] == B[i]:
                A[i:k+1] = A[i:k+1][::-1]
                swap_count += 1
                break
        else:
            print(-1)
            break
    i += 1
else:
    print(swap_count)
