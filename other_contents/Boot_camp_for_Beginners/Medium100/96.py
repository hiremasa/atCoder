MOD = 10**9 + 7
 
N,M = map(int,input().split())
dp = [0]*(N+1)
dp[0] = 1
A = set(int(input()) for _ in range(M))


for i in range(1, N + 1):
    if i in A:
        continue
    x = dp[i - 1]
    if i > 1:
        x += dp[i - 2]
    dp[i] = x % MOD
answer = dp[N]
print(answer)