q = int(input())

def LCS(A, B):
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

    for i, a in enumerate(A):
        for j, b in enumerate(B):

            if a == b:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[len(A)][len(B)]

for _ in range(q):
    A = input()
    B = input()

    print(LCS(A, B))