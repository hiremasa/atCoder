N, M = map(int, input().split())
C = list(map(int, input().split()))

dp = [[float("inf")] * (N + 1) for _ in range(M + 1)]
dp[0][0] = 0
for i in range(M):
    c = C[i]
    for n in range(N + 1):
        if n - c >= 0:
            dp[i + 1][n] = min(dp[i + 1][n - c] + 1, dp[i][n])
        else:
            dp[i + 1][n] = dp[i][n]
#print(dp)
print(dp[M][N])
