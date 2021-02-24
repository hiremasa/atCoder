from collections import Counter, defaultdict

N = int(input())
dd = defaultdict(int)

for _ in range(N):
    s = str(sorted(input()))
    dd[s] += 1

ans = 0
for k, v in dd.items():
    if v >= 2:
        ans += v * (v-1) // 2
print(ans)
