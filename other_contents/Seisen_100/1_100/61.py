N, M = map(int, input().split())

G = [[float("inf")] * N for _ in range(N)]
for i in range(N):
    G[i][i] = 0

for _ in range(M):
    a, b, t = map(int, input().split())
    G[a - 1][b - 1] = t
    G[b - 1][a - 1] = t

for k in range(N):
    for i in range(N):
        for j in range(N):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

temp_min = float("inf")
ans = 0
for i in range(N):
    temp = max(G[i])
    if temp_min > temp:
        ans = i
        temp_min = temp
print(max(G[ans][i] for i in range(N) if i != ans))
