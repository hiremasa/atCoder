N, W = map(int, input().split())

dp = [[0] * (W + 1) for _ in range(N + 1)]

items = []

for i in range(N):
    v, w = map(int, input().split())
    items.append([v,w])

for i in range(1, N + 1):
    v_item, w_item = items[i- 1]

    for w in range(W + 1):
        if w >= w_item:
            dp[i][w] = max(dp[i][w - w_item] + v_item,\
                        dp[i - 1][w - w_item] + v_item,\
                        dp[i - 1][w])
        else:
            dp[i][w] = dp[i - 1][w]
#print(dp)
print(dp[N][W])
