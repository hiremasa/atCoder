N, M = map(int, input().split())

AB = []
for _ in range(M):
    a, b = map(int, input().split())
    AB.append([a, b])

ans = "IMPOSSIBLE"
for i in range(2, N+1):
    if [1, i] in AB and [i, N] in AB:
        ans = "POSSIBLE"

print(ans)
