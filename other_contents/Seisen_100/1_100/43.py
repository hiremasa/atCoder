N = int(input())
S = [list(input()) for _ in range(5)]
#print(S)
dp = [[float("inf")] * 3 for _ in range(N)]
Colors = ["R", "B", "W"]

#init
def calc_num_change(S, S_index, color):
    s = [s[S_index] for s in S]# 列を取り出す
    #print(s)
    return len([i for i in s if i != color])

for i in range(3):
    dp[0][i] = calc_num_change(S, 0, Colors[i])

#更新
for i in range(N - 1):
    for c in range(3):
        cost = calc_num_change(S, i + 1, Colors[c])
        #print(f"row: {i + 1}, color: {c, Colors[c]}, cost: {cost}")
        for j, color in enumerate(Colors):
            if color != Colors[c]:
                dp[i + 1][c] = min(dp[i][j] + cost, dp[i + 1][c])
print(min(dp[-1]))
