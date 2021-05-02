#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

dp = [[float('inf')]*(M+1) for _ in range(N+1)]

for i in range(M+1): dp[0][i] = 0

for i in range(N):
    for j in range(i+1, M+1):
        for k in range(0, j):
            dp[i+1][j] = min(dp[i+1][j], dp[i][k] + C[k]*D[i])

ans = float('inf')
for i in range(M+1):
    ans = min(ans, dp[N][i])
print(ans)

# for row in dp:
#     print(*row)