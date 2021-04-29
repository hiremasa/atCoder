N, K = map(int, input().split())
dp = [[0] * 3 for _ in range(N　+ 1)]
AB = {}
for _ in range(K):
    a, b = map(int, input().split())
    AB.append([a, b - 1])
sorted(AB, key=lambda x: x[0])
for a, b in AB.items():
    if a == 1:
        dp[1][b - 1] = 1
    if a == 2:
        dp[2][b - 1] = sum([dp[1][i] for i in range(3)])
    if a >= 3:
        break

for i in range(3, N + 1):
    if 
