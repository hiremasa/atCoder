

D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
A, B, C = [], [], []
for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

dp = [[0] * N for _ in range(D)]

#init
for i in range(D):
    for j in range(N):
        if not A[j] <= T[i] <= B[j]:
            dp[i][j] = -1

#更新

for i in range(D - 1):
    for j in range(N):
        if dp[i][j] == -1:
            continue
        else:
            for k in range(N):
                if dp[i + 1][k] != -1:
                    dp[i + 1][k] = max(dp[i + 1][k], abs(C[k] - C[j]) + dp[i][j])
print(max(dp[-1]))
