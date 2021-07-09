# N, B, K = map(int, input().split())
# C = list(map(int, input().split()))
# mod = 10**9 + 7
# dp = [[0] * N for _ in range(B)]


#============O(NBK)
#init
# for k in range(K):
#     dp[C[k] % B][0] += 1

# for n in range(N - 1):
#     for b in range(B):
#         for k in range(K):
#             dp[(C[k] + b * 10) % B][n + 1] += dp[b][n] % mod
#             dp[(C[k] + b * 10) % B][n + 1] %= mod

# print(dp[0][-1])

import numpy as np
N, B, K = map(int, input().split())
C = list(map(int, input().split()))
mod = 10**9 + 7

A = [[0] * B for _ in range(B)]
for i in range(B):
    for k in range(K):
        A[(10 * i + C[k]) % B][i] = 1

print(A)

A_K = np.linalg.matrix_power(np.array(A), K - 1)

dp = [0] * B
#init
for k in range(K):
    dp[C[k] % B] += 1

ans = np.dot(A_K, np.array(dp))
print(ans)