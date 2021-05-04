
N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

dp = [[float("inf")] * (M + 1) for _ in range(N + 1)]

#init
for i in range(M + 1):
    dp[0][i] = 0

#更新
for i in range(N):
    for j in range(M):
        dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j] + C[j] * D[i])


ans = float('inf')
for i in range(M + 1):
    ans = min(ans, dp[N][i])
print(ans)


