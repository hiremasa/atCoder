N, M = map(int, input().split())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))

CD = []
for _ in range(M):
    c, d = map(int, input().split())
    CD.append((c, d))


for a, b in AB:
    ans = 0
    distance = float("inf")
    for i in range(M):
        c, d = CD[i]
        temp = abs(a - c) + abs(b - d)
        if temp < distance:
            ans = i
            distance = temp
    print(ans + 1)
