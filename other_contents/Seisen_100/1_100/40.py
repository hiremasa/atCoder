"""
from collections import defaultdict
D=defaultdict(int)

MOD = 10**4
N, K = map(int, input().split())

DP = [[[0] * 3 for i in range(3)] for j in range(N + 1)] #dp[i][j][k] := i日目までに１日前j、２日前kを食べたときの総数
for _ in range(K):
    a, b = map(int, input().split())
    D[a] = b

if D[1]==0: #1日目に指定なし
    if D[2]==0: #2日目に指定なし①
        for i in range(3):
            for j in range(3):
                DP[2][i][j] = 1
    else: #2日目に指定あり②
        for i in range(3):
            DP[2][i][D[2] - 1] = 1
elif D[2] == 0: #1日目に指定あり、かつ2日目に指定なし③
    for i in range(3):
        DP[2][D[1] - 1][i] = 1
else: #1日目に指定あり、かつ2日目に指定あり④
    DP[2][D[1] - 1][D[2] - 1] = 1

for i in range(2, N):
    # i日目に指定なし
    if D[i + 1] == 0:
        for j in range(3):
            for k in range(3):
                DP[i + 1][j][k] = sum([DP[i][j_][k_] for j_ in range(3) for k_ in range(3)]) % MOD
                if j == k: #余分を引く
                    DP[i + 1][j][k] -= DP[i + 1][j][k] % MOD
    #i日目に指定あり
    else:
        shitei = DP[i + 1] - 1
        for j in range(3):
            DP[i + 1][j][shitei] = sum([DP[i][temp][shitei] for temp in range(3)])
            if shitei == j:
                DP[i + 1][j][shitei]-=DP[i][j][shitei]

ans = 0
for i in range(3):
  for j in range(3):
    ans+=DP[-1][i][j] % MOD
print(ans % MOD)
"""


#=========================================

import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, K = [int(x) for x in input().split()]
    AB = [[int(x) for x in input().split()] for _ in range(K)]

    MOD = 10000

    dp = [[0] * 3 for j in range(N + 1)]

    for a, b in AB:
        if a == 1:
            dp[1][b - 1] = 1
            break
    else:
        dp[1][0] = 1
        dp[1][1] = 1
        dp[1][2] = 1

    for i in range(1, N):
        for j in range(3):
            for a, b in AB:
                if a == i + 1: #指定がある
                    if b - 1 == j: #指定のcol
                        if dp[i][j] == 0:
                            continue
                        if dp[i - 1][j] == 0:
                            dp[i + 1][j] += dp[i][j]
                        else:
                            dp[i + 1][j] += max(0, sum(dp[i - 1]) - dp[i - 1][j])
                    else: #指定があるけど、指定のcolじゃない
                        dp[i + 1][b - 1] += dp[i][j]
                    break
            else:
                if dp[i][j] == 0:
                    continue
                if dp[i - 1][j] == 0:
                    dp[i + 1][j] += dp[i][j]
                else:
                    dp[i + 1][j] += max(0, sum(dp[i - 1]) - dp[i - 1][j])
                dp[i + 1][(j + 1) % 3] += dp[i][j]
                dp[i + 1][(j + 2) % 3] += dp[i][j]

    print(sum(dp[N]) % MOD)


if __name__ == '__main__':
    main()
