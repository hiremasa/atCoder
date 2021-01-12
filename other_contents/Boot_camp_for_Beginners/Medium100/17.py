N, T = map(int, input().split())
TT = list(map(int, input().split()))

ans = T
now = 0
for t in TT[1:]:
    ans += min(T, t - now)
    now = t
print(ans)