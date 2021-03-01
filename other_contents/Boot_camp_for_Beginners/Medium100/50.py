N, M = map(int, input().split())

if M - N >= 2019:
    exit(print(0))

ans = 2018
for i in range(N, M +1):
    for j in range(i + 1, M + 1):
        temp = (i * j) % 2019
        ans = min(ans, temp)
print(ans)