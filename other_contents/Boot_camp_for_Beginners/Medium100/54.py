n, c, k = map(int, input().split())
t = [int(input()) for _ in range(n)]
t.sort()
ans = 0
m = 0
limit = float('inf')
for x in t:
    if m == c or limit < x:
        ans += 1
        m = 0
    if m == 0:
        limit = x + k
    m += 1
if m:
    ans += 1
print(ans)
