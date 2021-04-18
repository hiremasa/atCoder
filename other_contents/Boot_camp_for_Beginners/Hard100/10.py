N, K = map(int, input().split())
A = list(map(int, input().split()))

s = 0
l = 0
ans = 0

for r in range(N):
    s += A[r]
    while s >= K:
        s -= A[l]
        l += 1
    ans += l
print(ans)