N, K = map(int, input().split())
ans = 0
for i in range(1, N+1):
    a = 0
    while i * 2**a <= (K-1):
        a += 1
    ans += 1/N * (1/2)**a
print(ans)